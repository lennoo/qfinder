#{{{-----------------------------------------------------------
#
# QGIS Quick Finder Plugin
# Copyright (C) 2014 Denis Rouzaud, Anrnaud Morvan
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#--------------------------------------------------------------------}}}

import json
from builtins import range
from urllib import request, parse
from qgis.PyQt.QtCore import Qt, QCoreApplication, pyqtSignal, QEventLoop, QUrl
from qgis.PyQt.QtGui import QIcon, QColor, QCursor 
from qgis.PyQt.QtWidgets import QComboBox, QSizePolicy, QTreeView, QApplication, QPushButton, QHBoxLayout 
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply

from qgis.core import QgsGeometry, QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject, QgsMessageLog, QgsRectangle, QgsPointXY, Qgis, QgsWkbTypes
from qgis.core import *
from qgis.gui import QgsRubberBand, QgsVertexMarker

from ..core.http_finder import HttpFinder
from ..core.my_settings import MySettings
from .result_model import ResultModel, GroupItem, ResultItem


class FinderBox(QComboBox):

    running = False
    to_finish = 0

    search_started = pyqtSignal()
    search_finished = pyqtSignal()

    def __init__(self, finders, iface, parent=None):
        self.iface = iface
        self.mapCanvas = iface.mapCanvas()
        self.marker = None
        self.rubber = QgsRubberBand(self.mapCanvas)
        self.rubber.setColor(QColor(255, 255, 50, 200))
        self.rubber.setIcon(self.rubber.ICON_CIRCLE)
        self.rubber.setIconSize(15)
        self.rubber.setWidth(4)
        self.rubber.setBrushStyle(Qt.NoBrush)

        QComboBox.__init__(self, parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.InsertAtTop)
        self.setMinimumHeight(27)
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Fixed)

        self.insertSeparator(0)
        self.lineEdit().returnPressed.connect(self.search)

        self.result_view = QTreeView()
        self.result_view.setHeaderHidden(True)
        self.result_view.setMinimumHeight(300)
        self.result_view.activated.connect(self.itemActivated)
        self.result_view.pressed.connect(self.itemPressed)
        self.setView(self.result_view)

        self.result_model = ResultModel(self)
        self.setModel(self.result_model)

        self.finders = finders
        for finder in list(self.finders.values()):
            finder.result_found.connect(self.result_found)
            finder.limit_reached.connect(self.limit_reached)
            finder.finished.connect(self.finished)

        self.clearButton = QPushButton(self)
        self.clearButton.setIcon(QIcon(":/plugins/quickfinder/icons/draft.svg"))
        self.clearButton.setText('')
        self.clearButton.setFlat(True)
        self.clearButton.setCursor(QCursor(Qt.ArrowCursor))
        self.clearButton.setStyleSheet('border: 0px; padding: 0px;')
        self.clearButton.clicked.connect(self.clear)

        layout = QHBoxLayout(self)
        self.setLayout(layout)
        layout.addStretch()
        layout.addWidget(self.clearButton)
        layout.addSpacing(20)

        button_size = self.clearButton.sizeHint()
        # frameWidth = self.lineEdit().style().pixelMetric(QtGui.QStyle.PM_DefaultFrameWidth)
        padding = button_size.width()  # + frameWidth + 1
        self.lineEdit().setStyleSheet('QLineEdit {padding-right: %dpx; }' % padding)

    def __del__(self):
        if self.rubber:
            self.iface.mapCanvas().scene().removeItem(self.rubber)
            del self.rubber

    #clear marker that the lonlat seted
    def clearMarker(self):
        self.mapCanvas.scene().removeItem(self.marker)
        self.marker = None

    def clearSelection(self):
        self.result_model.setSelected(None, self.result_view.palette())
        self.rubber.reset()
        #self.clearMarker()

    def clear(self):
        self.clearSelection()
        self.result_model.clearResults()
        self.lineEdit().setText('')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.clearSelection()
            self.clearMarker()
        QComboBox.keyPressEvent(self, event)
    
    def lnglatFinder(self, to_find):
        import re
        m = re.match(r'(?P<lon>-?\d*(.\d+))\s+(?P<lat>-?\d*(.\d+))',to_find)
        if not m :
            return False
        x = float(m.group('lon'))
        y = float(m.group('lat'))
        return self.zoomLnglat(x,y)

    def zoomLnglat(self, lng, lat):
        x, y = lng, lat

        canvas = self.mapCanvas
        currExt = canvas.extent()
        canvasCenter = currExt.center()
        dx = float(x) - canvasCenter.x()
        dy = float(y) - canvasCenter.y()
		
        xMin = currExt.xMinimum() + dx
        xMax = currExt.xMaximum() + dx
        yMin = currExt.yMinimum() + dy
        yMax = currExt.yMaximum() + dy

        rect = QgsRectangle(xMin,yMin,xMax,yMax)
        canvas.setExtent(rect)
        pt = QgsPointXY(float(x),float(y))
        self.marker = QgsVertexMarker(canvas)
        self.marker.setCenter(pt)
        self.marker.setIconSize(18)
        self.marker.setPenWidth(2)
        self.marker.setIconType(QgsVertexMarker.ICON_CROSS)
        canvas.refresh()
        return True

#    def geocodeFinder(self, to_finder):
#        print(to_finder[:2])
#        if not to_finder[:2] == 'b:':
#            return False
#
#        address = to_finder[2:] 
#        url = MySettings().value("baiduUrl")
#        url = url + parse.quote(address)
#
#        response = request.urlopen(url)
#        content = response.read()
#        data = json.loads(content)
#        print(data)
#        lng, lat = (data['result']['location']['lng'], data['result']['location']['lat'])
#        from .cood_trans import bd09_to_wgs84
#        lng, lat = bd09_to_wgs84(lng, lat)
#        print(f'{lng}-{lat}')
#        return self.zoomLnglat(lng, lat)


    def search(self):
      #  self.geocode()
        if self.running:
            return

        to_find = self.lineEdit().text()
        if not to_find or to_find == '':
            return
#        if not (self.lnglatFinder(to_find) or self.geocodeFinder(to_find)):
        if not self.lnglatFinder(to_find):
            self.showPopup()

        self.running = True
        self.search_started.emit()

        self.clearSelection()
        self.result_model.clearResults()
        self.result_model.truncateHistory(MySettings().value("historyLength"))
        self.result_model.setLoading(True)

        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)

        self.finders_to_start = []
        for finder in list(self.finders.values()):
            if finder.activated():
                self.finders_to_start.append(finder)

        bbox = self.mapCanvas.fullExtent()

        while len(self.finders_to_start) > 0:
            finder = self.finders_to_start[0]
            self.finders_to_start.remove(finder)
            self.result_model.addResult(finder.name)
            finder.start(to_find, bbox=bbox)

        # For case there is no finder activated
        self.finished(None)

    def stop(self):
        self.finders_to_start = []
        for finder in list(self.finders.values()):
            if finder.is_running():
                finder.stop()
        self.finished(None)

    def result_found(self, finder, layername, value, geometry, srid):
        self.result_model.addResult(finder.name, layername, value, geometry, srid)
        self.result_view.expandAll()

    def limit_reached(self, finder, layername):
        self.result_model.addEllipsys(finder.name, layername)

    def finished(self, finder):
        if len(self.finders_to_start) > 0:
            return
        for finder in list(self.finders.values()):
            if finder.is_running():
                return

        self.running = False
        self.search_finished.emit()

        self.result_model.setLoading(False)

        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)

    def itemActivated(self, index):
        item = self.result_model.itemFromIndex(index)
        self.showItem(item)

    def itemPressed(self, index):
        item = self.result_model.itemFromIndex(index)
        if QApplication.mouseButtons() == Qt.LeftButton:
            self.showItem(item)

    def showItem(self, item):
        if isinstance(item, ResultItem):
            self.result_model.setSelected(item, self.result_view.palette())
            geometry = self.transform_geom(item)
            self.rubber.reset(geometry.type())
            self.rubber.setToGeometry(geometry, None)
            self.zoom_to_rubberband()
            return

        if isinstance(item, GroupItem):
            child = item.child(0)
            if isinstance(child, ResultItem):
                self.result_model.setSelected(item, self.result_view.palette())
                self.rubber.reset(child.geometry.type())
                for i in range(0, item.rowCount()):
                    geometry = self.transform_geom(item.child(i))
                    self.rubber.addGeometry(geometry, None)
                self.zoom_to_rubberband()
            return

        if item.__class__.__name__ == 'QStandardItem':
            self.clearSelection()

    def transform_geom(self, item):
        src_crs = QgsCoordinateReferenceSystem()
        src_crs.createFromSrid(item.srid)
        dest_crs = self.mapCanvas.mapSettings().destinationCrs()
        geom = QgsGeometry(item.geometry)
        geom.transform(QgsCoordinateTransform(src_crs, dest_crs, QgsProject.instance()))
        return geom

    def zoom_to_rubberband(self):
        geom = self.rubber.asGeometry()
        if geom:
            rect = geom.boundingBox()
            rect.scale(1.5)
            self.mapCanvas.setExtent(rect)
            self.mapCanvas.refresh()
