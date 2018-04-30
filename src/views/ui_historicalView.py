# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historicalView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistoricalDialog(object):
    def setupUi(self, HistoricalDialog):
        HistoricalDialog.setObjectName("HistoricalDialog")
        HistoricalDialog.resize(912, 528)
        self.verticalLayout = QtWidgets.QVBoxLayout(HistoricalDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(HistoricalDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.ImportTab = QtWidgets.QWidget()
        self.ImportTab.setObjectName("ImportTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ImportTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hBoxMainImport = QtWidgets.QHBoxLayout()
        self.hBoxMainImport.setObjectName("hBoxMainImport")
        self.vBoxLabels = QtWidgets.QVBoxLayout()
        self.vBoxLabels.setContentsMargins(30, 22, 30, -1)
        self.vBoxLabels.setSpacing(30)
        self.vBoxLabels.setObjectName("vBoxLabels")
        self.labelInputFormat = QtWidgets.QLabel(self.ImportTab)
        self.labelInputFormat.setObjectName("labelInputFormat")
        self.vBoxLabels.addWidget(self.labelInputFormat, 0, QtCore.Qt.AlignLeft)
        self.labelTimeZone = QtWidgets.QLabel(self.ImportTab)
        self.labelTimeZone.setObjectName("labelTimeZone")
        self.vBoxLabels.addWidget(self.labelTimeZone, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vBoxLabels.addItem(spacerItem)
        self.hBoxMainImport.addLayout(self.vBoxLabels)
        self.vBoxLeftImport = QtWidgets.QVBoxLayout()
        self.vBoxLeftImport.setContentsMargins(-1, 15, 30, -1)
        self.vBoxLeftImport.setSpacing(25)
        self.vBoxLeftImport.setObjectName("vBoxLeftImport")
        self.comboInputFormat = QtWidgets.QComboBox(self.ImportTab)
        self.comboInputFormat.setObjectName("comboInputFormat")
        self.vBoxLeftImport.addWidget(self.comboInputFormat)
        self.comboTimeZone = QtWidgets.QComboBox(self.ImportTab)
        self.comboTimeZone.setObjectName("comboTimeZone")
        self.vBoxLeftImport.addWidget(self.comboTimeZone)
        self.btnImport = QtWidgets.QPushButton(self.ImportTab)
        self.btnImport.setObjectName("btnImport")
        self.vBoxLeftImport.addWidget(self.btnImport, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vBoxLeftImport.addItem(spacerItem1)
        self.hBoxMainImport.addLayout(self.vBoxLeftImport)
        self.hBoxMainImport.setStretch(0, 1)
        self.hBoxMainImport.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.hBoxMainImport)
        self.tabWidget.addTab(self.ImportTab, "")
        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DownloadTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelSymbols = QtWidgets.QLabel(self.DownloadTab)
        self.labelSymbols.setObjectName("labelSymbols")
        self.verticalLayout_2.addWidget(self.labelSymbols)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineFilter = QtWidgets.QLineEdit(self.DownloadTab)
        self.lineFilter.setObjectName("lineFilter")
        self.horizontalLayout_3.addWidget(self.lineFilter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButtonClearAll = QtWidgets.QToolButton(self.DownloadTab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/clearall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonClearAll.setIcon(icon)
        self.toolButtonClearAll.setObjectName("toolButtonClearAll")
        self.horizontalLayout.addWidget(self.toolButtonClearAll)
        self.toolButtonDelete = QtWidgets.QToolButton(self.DownloadTab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonDelete.setIcon(icon1)
        self.toolButtonDelete.setObjectName("toolButtonDelete")
        self.horizontalLayout.addWidget(self.toolButtonDelete)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.listViewImported = QtWidgets.QListView(self.DownloadTab)
        self.listViewImported.setObjectName("listViewImported")
        self.verticalLayout_2.addWidget(self.listViewImported)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.vBoxRightDownload = QtWidgets.QVBoxLayout()
        self.vBoxRightDownload.setObjectName("vBoxRightDownload")
        self.labelDatabaseCount = QtWidgets.QLabel(self.DownloadTab)
        self.labelDatabaseCount.setObjectName("labelDatabaseCount")
        self.vBoxRightDownload.addWidget(self.labelDatabaseCount)
        self.ohlcTableView = AkTableView(self.DownloadTab)
        self.ohlcTableView.setObjectName("ohlcTableView")
        self.vBoxRightDownload.addWidget(self.ohlcTableView)
        self.groupBoxFilter = QtWidgets.QGroupBox(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxFilter.sizePolicy().hasHeightForWidth())
        self.groupBoxFilter.setSizePolicy(sizePolicy)
        self.groupBoxFilter.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBoxFilter.setObjectName("groupBoxFilter")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxFilter)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vBoxFilter = QtWidgets.QVBoxLayout()
        self.vBoxFilter.setObjectName("vBoxFilter")
        self.fBoxFilterDate = QtWidgets.QFormLayout()
        self.fBoxFilterDate.setContentsMargins(-1, -1, -1, 5)
        self.fBoxFilterDate.setHorizontalSpacing(30)
        self.fBoxFilterDate.setObjectName("fBoxFilterDate")
        self.labelStartDate = QtWidgets.QLabel(self.groupBoxFilter)
        self.labelStartDate.setObjectName("labelStartDate")
        self.fBoxFilterDate.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelStartDate)
        self.dateStart = QtWidgets.QDateEdit(self.groupBoxFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateStart.sizePolicy().hasHeightForWidth())
        self.dateStart.setSizePolicy(sizePolicy)
        self.dateStart.setObjectName("dateStart")
        self.fBoxFilterDate.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateStart)
        self.labelEndDate = QtWidgets.QLabel(self.groupBoxFilter)
        self.labelEndDate.setObjectName("labelEndDate")
        self.fBoxFilterDate.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelEndDate)
        self.dateEnd = QtWidgets.QDateEdit(self.groupBoxFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEnd.sizePolicy().hasHeightForWidth())
        self.dateEnd.setSizePolicy(sizePolicy)
        self.dateEnd.setObjectName("dateEnd")
        self.fBoxFilterDate.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEnd)
        self.vBoxFilter.addLayout(self.fBoxFilterDate)
        self.btnFilter = QtWidgets.QPushButton(self.groupBoxFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFilter.sizePolicy().hasHeightForWidth())
        self.btnFilter.setSizePolicy(sizePolicy)
        self.btnFilter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnFilter.setObjectName("btnFilter")
        self.vBoxFilter.addWidget(self.btnFilter, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.vBoxFilter)
        self.vBoxRightDownload.addWidget(self.groupBoxFilter)
        self.horizontalLayout_4.addLayout(self.vBoxRightDownload)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.DownloadTab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(HistoricalDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HistoricalDialog)

    def retranslateUi(self, HistoricalDialog):
        _translate = QtCore.QCoreApplication.translate
        HistoricalDialog.setWindowTitle(_translate("HistoricalDialog", "Dialog"))
        self.labelInputFormat.setText(_translate("HistoricalDialog", "Data Input Format: "))
        self.labelTimeZone.setText(_translate("HistoricalDialog", "Time zone of imported data: "))
        self.btnImport.setText(_translate("HistoricalDialog", "Start Import"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImportTab), _translate("HistoricalDialog", "Import"))
        self.labelSymbols.setText(_translate("HistoricalDialog", "Symbols: "))
        self.toolButtonClearAll.setText(_translate("HistoricalDialog", "Clear"))
        self.toolButtonDelete.setText(_translate("HistoricalDialog", "Del"))
        self.labelDatabaseCount.setText(_translate("HistoricalDialog", "Database: "))
        self.groupBoxFilter.setTitle(_translate("HistoricalDialog", "Filter Data"))
        self.labelStartDate.setText(_translate("HistoricalDialog", "Start date: "))
        self.labelEndDate.setText(_translate("HistoricalDialog", "End date: "))
        self.btnFilter.setText(_translate("HistoricalDialog", "Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DownloadTab), _translate("HistoricalDialog", "Instruments"))

from src.controls.akTableView import AkTableView
import src.Resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistoricalDialog = QtWidgets.QDialog()
    ui = Ui_HistoricalDialog()
    ui.setupUi(HistoricalDialog)
    HistoricalDialog.show()
    sys.exit(app.exec_())

