# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_projectsearch.ui'
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

class Ui_ProjectSearch(object):
    def setupUi(self, ProjectSearch):
        ProjectSearch.setObjectName(_fromUtf8("ProjectSearch"))
        ProjectSearch.resize(282, 295)
        self.formLayout = QtWidgets.QFormLayout(ProjectSearch)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtWidgets.QLabel(ProjectSearch)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.searchName = QtWidgets.QLineEdit(ProjectSearch)
        self.searchName.setObjectName(_fromUtf8("searchName"))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchName)
        self.layerLabel = QtWidgets.QLabel(ProjectSearch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerLabel.sizePolicy().hasHeightForWidth())
        self.layerLabel.setSizePolicy(sizePolicy)
        self.layerLabel.setObjectName(_fromUtf8("layerLabel"))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.layerLabel)
        self.layerCombo = QgsMapLayerComboBox(ProjectSearch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerCombo.sizePolicy().hasHeightForWidth())
        self.layerCombo.setSizePolicy(sizePolicy)
        self.layerCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.layerCombo.setObjectName(_fromUtf8("layerCombo"))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.layerCombo)
        self.FieldNameLabel = QtWidgets.QLabel(ProjectSearch)
        self.FieldNameLabel.setObjectName(_fromUtf8("FieldNameLabel"))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.FieldNameLabel)
        self.fieldExpressionWidget = QgsFieldExpressionWidget(ProjectSearch)
        self.fieldExpressionWidget.setObjectName(_fromUtf8("fieldExpressionWidget"))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fieldExpressionWidget)
        self.label_2 = QtWidgets.QLabel(ProjectSearch)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.priorityBox = QtWidgets.QSpinBox(ProjectSearch)
        self.priorityBox.setMinimum(1)
        self.priorityBox.setMaximum(999)
        self.priorityBox.setProperty("value", 1)
        self.priorityBox.setObjectName(_fromUtf8("priorityBox"))
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.priorityBox)
        self.progressBar = QtWidgets.QProgressBar(ProjectSearch)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.evaluateCheckBox = QtWidgets.QCheckBox(ProjectSearch)
        self.evaluateCheckBox.setChecked(True)
        self.evaluateCheckBox.setObjectName(_fromUtf8("evaluateCheckBox"))
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.evaluateCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(ProjectSearch)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(ProjectSearch)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.formLayout.setLayout(11, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.geometryStorageLabel = QtWidgets.QLabel(ProjectSearch)
        self.geometryStorageLabel.setObjectName(_fromUtf8("geometryStorageLabel"))
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.geometryStorageLabel)
        self.geometryStorageCombo = QtWidgets.QComboBox(ProjectSearch)
        self.geometryStorageCombo.setObjectName(_fromUtf8("geometryStorageCombo"))
        self.geometryStorageCombo.addItem(_fromUtf8(""))
        self.geometryStorageCombo.addItem(_fromUtf8(""))
        self.geometryStorageCombo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.geometryStorageCombo)

        self.retranslateUi(ProjectSearch)
        QtCore.QMetaObject.connectSlotsByName(ProjectSearch)
        ProjectSearch.setTabOrder(self.searchName, self.layerCombo)
        ProjectSearch.setTabOrder(self.layerCombo, self.geometryStorageCombo)
        ProjectSearch.setTabOrder(self.geometryStorageCombo, self.priorityBox)
        ProjectSearch.setTabOrder(self.priorityBox, self.evaluateCheckBox)
        ProjectSearch.setTabOrder(self.evaluateCheckBox, self.cancelButton)
        ProjectSearch.setTabOrder(self.cancelButton, self.okButton)

    def retranslateUi(self, ProjectSearch):
        ProjectSearch.setWindowTitle(_translate("ProjectSearch", "QuickFinder :: project search", None))
        self.label.setText(_translate("ProjectSearch", "Search name", None))
        self.layerLabel.setText(_translate("ProjectSearch", "Layer", None))
        self.FieldNameLabel.setText(_translate("ProjectSearch", "Field", None))
        self.label_2.setText(_translate("ProjectSearch", "Priority", None))
        self.evaluateCheckBox.setToolTip(_translate("ProjectSearch", "<html><head/><body><p>If checked, the search entries will be recorded directly.</p><p>If you want to add several large layers, uncheck it and use the refresh button once all layers have been added.</p></body></html>", None))
        self.evaluateCheckBox.setText(_translate("ProjectSearch", "record entries", None))
        self.cancelButton.setText(_translate("ProjectSearch", "Cancel", None))
        self.okButton.setText(_translate("ProjectSearch", "OK", None))
        self.geometryStorageLabel.setText(_translate("ProjectSearch", "Geometry storage", None))
        self.geometryStorageCombo.setItemText(0, _translate("ProjectSearch", "wkb", None))
        self.geometryStorageCombo.setItemText(1, _translate("ProjectSearch", "wkt", None))
        self.geometryStorageCombo.setItemText(2, _translate("ProjectSearch", "extent", None))

from qgis.gui import QgsFieldExpressionWidget, QgsMapLayerComboBox
