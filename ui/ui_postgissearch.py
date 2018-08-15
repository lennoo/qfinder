# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_postgissearch.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PostgisSearch(object):
    def setupUi(self, PostgisSearch):
        PostgisSearch.setObjectName(_fromUtf8("PostgisSearch"))
        PostgisSearch.resize(551, 368)
        self.gridLayout = QtGui.QGridLayout(PostgisSearch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(PostgisSearch)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(PostgisSearch)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.queryEdit = QtGui.QTextEdit(PostgisSearch)
        self.queryEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.queryEdit.setAcceptRichText(False)
        self.queryEdit.setObjectName(_fromUtf8("queryEdit"))
        self.gridLayout.addWidget(self.queryEdit, 2, 1, 1, 2)
        self.srid = QtGui.QLineEdit(PostgisSearch)
        self.srid.setEnabled(True)
        self.srid.setInputMask(_fromUtf8(""))
        self.srid.setReadOnly(True)
        self.srid.setObjectName(_fromUtf8("srid"))
        self.gridLayout.addWidget(self.srid, 3, 1, 1, 1)
        self.postgisCrsButton = QtGui.QPushButton(PostgisSearch)
        self.postgisCrsButton.setObjectName(_fromUtf8("postgisCrsButton"))
        self.gridLayout.addWidget(self.postgisCrsButton, 3, 2, 1, 1)
        self.postgisCrsLabel = QtGui.QLabel(PostgisSearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.postgisCrsLabel.sizePolicy().hasHeightForWidth())
        self.postgisCrsLabel.setSizePolicy(sizePolicy)
        self.postgisCrsLabel.setObjectName(_fromUtf8("postgisCrsLabel"))
        self.gridLayout.addWidget(self.postgisCrsLabel, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(PostgisSearch)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.project = QtGui.QCheckBox(PostgisSearch)
        self.project.setObjectName(_fromUtf8("project"))
        self.gridLayout.addWidget(self.project, 0, 1, 1, 1)
        self.FieldNameLabel = QtGui.QLabel(PostgisSearch)
        self.FieldNameLabel.setObjectName(_fromUtf8("FieldNameLabel"))
        self.gridLayout.addWidget(self.FieldNameLabel, 2, 0, 1, 1)
        self.searchName = QtGui.QLineEdit(PostgisSearch)
        self.searchName.setObjectName(_fromUtf8("searchName"))
        self.gridLayout.addWidget(self.searchName, 1, 1, 1, 2)
        self.label = QtGui.QLabel(PostgisSearch)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.priorityBox = QtGui.QSpinBox(PostgisSearch)
        self.priorityBox.setMinimum(1)
        self.priorityBox.setMaximum(999)
        self.priorityBox.setProperty("value", 1)
        self.priorityBox.setObjectName(_fromUtf8("priorityBox"))
        self.gridLayout.addWidget(self.priorityBox, 4, 1, 1, 1)

        self.retranslateUi(PostgisSearch)
        QtCore.QMetaObject.connectSlotsByName(PostgisSearch)
        PostgisSearch.setTabOrder(self.project, self.searchName)
        PostgisSearch.setTabOrder(self.searchName, self.queryEdit)
        PostgisSearch.setTabOrder(self.queryEdit, self.postgisCrsButton)
        PostgisSearch.setTabOrder(self.postgisCrsButton, self.priorityBox)
        PostgisSearch.setTabOrder(self.priorityBox, self.okButton)
        PostgisSearch.setTabOrder(self.okButton, self.cancelButton)
        PostgisSearch.setTabOrder(self.cancelButton, self.srid)

    def retranslateUi(self, PostgisSearch):
        PostgisSearch.setWindowTitle(_translate("PostgisSearch", "QuickFinder :: postgis search", None))
        self.cancelButton.setText(_translate("PostgisSearch", "Cancel", None))
        self.okButton.setText(_translate("PostgisSearch", "OK", None))
        self.queryEdit.setToolTip(_translate("PostgisSearch", "<html><head/><body><p>SELECT textfield, ST_AsBinary(wkb_geometry)::geometry</p><p> FROM searchtable</p><p> WHERE textfield LIKE %(search)s</p><p> LIMIT %(limit)s</p></body></html>", None))
        self.postgisCrsButton.setText(_translate("PostgisSearch", "Select", None))
        self.postgisCrsLabel.setText(_translate("PostgisSearch", "SRID", None))
        self.label_2.setText(_translate("PostgisSearch", "Priority", None))
        self.project.setText(_translate("PostgisSearch", "Project", None))
        self.FieldNameLabel.setText(_translate("PostgisSearch", "SQL Query", None))
        self.label.setText(_translate("PostgisSearch", "Search name", None))

from . import resources_rc
