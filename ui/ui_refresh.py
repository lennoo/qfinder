# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_refresh.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from qgis.PyQt import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Refresh(object):
    def setupUi(self, Refresh):
        Refresh.setObjectName(_fromUtf8("Refresh"))
        Refresh.resize(493, 249)
        self.gridLayout = QtWidgets.QGridLayout(Refresh)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtWidgets.QDialogButtonBox(Refresh)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.unevaluatedCheckBox = QtWidgets.QCheckBox(Refresh)
        self.unevaluatedCheckBox.setObjectName(_fromUtf8("unevaluatedCheckBox"))
        self.horizontalLayout.addWidget(self.unevaluatedCheckBox)
        self.unevalutedDaysSpinBox = QtWidgets.QSpinBox(Refresh)
        self.unevalutedDaysSpinBox.setMinimum(1)
        self.unevalutedDaysSpinBox.setMaximum(9999)
        self.unevalutedDaysSpinBox.setProperty("value", 10)
        self.unevalutedDaysSpinBox.setObjectName(_fromUtf8("unevalutedDaysSpinBox"))
        self.horizontalLayout.addWidget(self.unevalutedDaysSpinBox)
        self.label_2 = QtWidgets.QLabel(Refresh)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.deletedLayersCheckBox = QtWidgets.QCheckBox(Refresh)
        self.deletedLayersCheckBox.setChecked(True)
        self.deletedLayersCheckBox.setObjectName(_fromUtf8("deletedLayersCheckBox"))
        self.gridLayout.addWidget(self.deletedLayersCheckBox, 5, 0, 1, 1)
        self.unrecordedCheckBox = QtWidgets.QCheckBox(Refresh)
        self.unrecordedCheckBox.setObjectName(_fromUtf8("unrecordedCheckBox"))
        self.gridLayout.addWidget(self.unrecordedCheckBox, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Refresh)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.refreshButton = QtWidgets.QPushButton(Refresh)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.horizontalLayout_3.addWidget(self.refreshButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Refresh)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        self.selectionWidget = QtWidgets.QWidget(Refresh)
        self.selectionWidget.setObjectName(_fromUtf8("selectionWidget"))
        self.selectionLayout = QtWidgets.QHBoxLayout(self.selectionWidget)
        self.selectionLayout.setMargin(0)
        self.selectionLayout.setObjectName(_fromUtf8("selectionLayout"))
        self.label = QtWidgets.QLabel(self.selectionWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.selectionLayout.addWidget(self.label)
        self.selectionComboBox = QtWidgets.QComboBox(self.selectionWidget)
        self.selectionComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.selectionComboBox.setObjectName(_fromUtf8("selectionComboBox"))
        self.selectionComboBox.addItem(_fromUtf8(""))
        self.selectionComboBox.addItem(_fromUtf8(""))
        self.selectionLayout.addWidget(self.selectionComboBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.selectionLayout.addItem(spacerItem4)
        self.gridLayout.addWidget(self.selectionWidget, 1, 0, 1, 1)

        self.retranslateUi(Refresh)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Refresh.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Refresh.reject)
        QtCore.QMetaObject.connectSlotsByName(Refresh)

    def retranslateUi(self, Refresh):
        Refresh.setWindowTitle(_translate("Refresh", "Quick Finder - Refresh", None))
        self.unevaluatedCheckBox.setText(_translate("Refresh", "do not refresh searches evaluted less than", None))
        self.label_2.setText(_translate("Refresh", "days ago", None))
        self.deletedLayersCheckBox.setText(_translate("Refresh", "remove searches whose layer has been removed from QGIS project", None))
        self.unrecordedCheckBox.setText(_translate("Refresh", "only unrecorded entries", None))
        self.cancelButton.setText(_translate("Refresh", "cancel", None))
        self.refreshButton.setText(_translate("Refresh", "refresh", None))
        self.label.setText(_translate("Refresh", "refresh", None))
        self.selectionComboBox.setItemText(0, _translate("Refresh", "all layers", None))
        self.selectionComboBox.setItemText(1, _translate("Refresh", "only selected rows", None))

