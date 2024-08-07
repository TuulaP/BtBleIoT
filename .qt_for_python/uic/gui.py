# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Desktop\dipl_rad_python_app\ble_test_app\package\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageDevices = QtWidgets.QWidget()
        self.pageDevices.setObjectName("pageDevices")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pageDevices)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_discovered = QtWidgets.QLabel(self.pageDevices)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_discovered.setFont(font)
        self.label_discovered.setObjectName("label_discovered")
        self.gridLayout_2.addWidget(self.label_discovered, 0, 0, 1, 1)
        self.pushButton_clearOut = QtWidgets.QPushButton(self.pageDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clearOut.sizePolicy().hasHeightForWidth())
        self.pushButton_clearOut.setSizePolicy(sizePolicy)
        self.pushButton_clearOut.setObjectName("pushButton_clearOut")
        self.gridLayout_2.addWidget(self.pushButton_clearOut, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonScan = QtWidgets.QPushButton(self.pageDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonScan.sizePolicy().hasHeightForWidth())
        self.pushButtonScan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonScan.setFont(font)
        self.pushButtonScan.setObjectName("pushButtonScan")
        self.horizontalLayout.addWidget(self.pushButtonScan)
        self.pushButton_Conn = QtWidgets.QPushButton(self.pageDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Conn.sizePolicy().hasHeightForWidth())
        self.pushButton_Conn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Conn.setFont(font)
        self.pushButton_Conn.setObjectName("pushButton_Conn")
        self.horizontalLayout.addWidget(self.pushButton_Conn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_devinfo = QtWidgets.QLabel(self.pageDevices)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_devinfo.setFont(font)
        self.label_devinfo.setObjectName("label_devinfo")
        self.gridLayout_2.addWidget(self.label_devinfo, 0, 2, 1, 1)
        self.label_output = QtWidgets.QLabel(self.pageDevices)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.gridLayout_2.addWidget(self.label_output, 4, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.pageDevices)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.pageDevices)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 3)
        self.listWidget = QtWidgets.QListWidget(self.pageDevices)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.pageDevices)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.pageDevices)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 5, 0, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_Configuration = QtWidgets.QLabel(self.pageDevices)
        self.label_Configuration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Configuration.setObjectName("label_Configuration")
        self.horizontalLayout_5.addWidget(self.label_Configuration)
        self.pushButton_Configuration = QtWidgets.QPushButton(self.pageDevices)
        self.pushButton_Configuration.setObjectName("pushButton_Configuration")
        self.horizontalLayout_5.addWidget(self.pushButton_Configuration)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 2, 1, 1)
        self.stackedWidget.addWidget(self.pageDevices)
        self.page_services = QtWidgets.QWidget()
        self.page_services.setObjectName("page_services")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_services)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_output_2 = QtWidgets.QLabel(self.page_services)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_output_2.setFont(font)
        self.label_output_2.setObjectName("label_output_2")
        self.gridLayout_3.addWidget(self.label_output_2, 5, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.page_services)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 4, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.page_services)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_services)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.page_services)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.page_services)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 0, 1, 1)
        self.pushButton_clearOut_2 = QtWidgets.QPushButton(self.page_services)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clearOut_2.sizePolicy().hasHeightForWidth())
        self.pushButton_clearOut_2.setSizePolicy(sizePolicy)
        self.pushButton_clearOut_2.setObjectName("pushButton_clearOut_2")
        self.gridLayout_3.addWidget(self.pushButton_clearOut_2, 7, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_services)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_3.addWidget(self.textBrowser_3, 6, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Disconnect = QtWidgets.QPushButton(self.page_services)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Disconnect.sizePolicy().hasHeightForWidth())
        self.pushButton_Disconnect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Disconnect.setFont(font)
        self.pushButton_Disconnect.setObjectName("pushButton_Disconnect")
        self.horizontalLayout_2.addWidget(self.pushButton_Disconnect)
        self.pushButtonService = QtWidgets.QPushButton(self.page_services)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonService.sizePolicy().hasHeightForWidth())
        self.pushButtonService.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonService.setFont(font)
        self.pushButtonService.setObjectName("pushButtonService")
        self.horizontalLayout_2.addWidget(self.pushButtonService)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.listWidget_characteristics = QtWidgets.QListWidget(self.page_services)
        self.listWidget_characteristics.setObjectName("listWidget_characteristics")
        self.gridLayout_3.addWidget(self.listWidget_characteristics, 1, 2, 1, 1)
        self.pushButton_Characteristic = QtWidgets.QPushButton(self.page_services)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Characteristic.setFont(font)
        self.pushButton_Characteristic.setObjectName("pushButton_Characteristic")
        self.gridLayout_3.addWidget(self.pushButton_Characteristic, 2, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_services)
        self.page_heartrate = QtWidgets.QWidget()
        self.page_heartrate.setObjectName("page_heartrate")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_heartrate)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graph_heartrate = PlotWidget(self.page_heartrate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_heartrate.sizePolicy().hasHeightForWidth())
        self.graph_heartrate.setSizePolicy(sizePolicy)
        self.graph_heartrate.setObjectName("graph_heartrate")
        self.gridLayout_5.addWidget(self.graph_heartrate, 1, 0, 1, 2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser_HeartRate = QtWidgets.QTextBrowser(self.page_heartrate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_HeartRate.sizePolicy().hasHeightForWidth())
        self.textBrowser_HeartRate.setSizePolicy(sizePolicy)
        self.textBrowser_HeartRate.setObjectName("textBrowser_HeartRate")
        self.gridLayout_6.addWidget(self.textBrowser_HeartRate, 1, 1, 3, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.HRVLabel = QtWidgets.QLabel(self.page_heartrate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HRVLabel.sizePolicy().hasHeightForWidth())
        self.HRVLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.HRVLabel.setFont(font)
        self.HRVLabel.setObjectName("HRVLabel")
        self.horizontalLayout_3.addWidget(self.HRVLabel)
        self.lcdHeartRate = QtWidgets.QLCDNumber(self.page_heartrate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdHeartRate.sizePolicy().hasHeightForWidth())
        self.lcdHeartRate.setSizePolicy(sizePolicy)
        self.lcdHeartRate.setSizeIncrement(QtCore.QSize(1400, 1200))
        self.lcdHeartRate.setBaseSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdHeartRate.setFont(font)
        self.lcdHeartRate.setDigitCount(3)
        self.lcdHeartRate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdHeartRate.setProperty("intValue", 0)
        self.lcdHeartRate.setObjectName("lcdHeartRate")
        self.horizontalLayout_3.addWidget(self.lcdHeartRate)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 1, 0, 2, 1)
        self.pushButtonRecord = QtWidgets.QPushButton(self.page_heartrate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRecord.sizePolicy().hasHeightForWidth())
        self.pushButtonRecord.setSizePolicy(sizePolicy)
        self.pushButtonRecord.setObjectName("pushButtonRecord")
        self.gridLayout_6.addWidget(self.pushButtonRecord, 4, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonNotifyHR = QtWidgets.QPushButton(self.page_heartrate)
        self.pushButtonNotifyHR.setObjectName("pushButtonNotifyHR")
        self.verticalLayout.addWidget(self.pushButtonNotifyHR)
        self.gridLayout_6.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.buttonHRdisconnect = QtWidgets.QPushButton(self.page_heartrate)
        self.buttonHRdisconnect.setObjectName("buttonHRdisconnect")
        self.gridLayout_6.addWidget(self.buttonHRdisconnect, 4, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_heartrate)
        self.page_max30001 = QtWidgets.QWidget()
        self.page_max30001.setObjectName("page_max30001")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_max30001)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.max30001_graph = PlotWidget(self.page_max30001)
        self.max30001_graph.setObjectName("max30001_graph")
        self.gridLayout_4.addWidget(self.max30001_graph, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_HeartRateBMED = QtWidgets.QLabel(self.page_max30001)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_HeartRateBMED.setFont(font)
        self.label_HeartRateBMED.setObjectName("label_HeartRateBMED")
        self.verticalLayout_2.addWidget(self.label_HeartRateBMED)
        self.label_TrainingZoneBMED = QtWidgets.QLabel(self.page_max30001)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_TrainingZoneBMED.setFont(font)
        self.label_TrainingZoneBMED.setObjectName("label_TrainingZoneBMED")
        self.verticalLayout_2.addWidget(self.label_TrainingZoneBMED)
        self.label_biometricDataBMED = QtWidgets.QLabel(self.page_max30001)
        self.label_biometricDataBMED.setObjectName("label_biometricDataBMED")
        self.verticalLayout_2.addWidget(self.label_biometricDataBMED)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.BMED_textbrowser = QtWidgets.QTextBrowser(self.page_max30001)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BMED_textbrowser.sizePolicy().hasHeightForWidth())
        self.BMED_textbrowser.setSizePolicy(sizePolicy)
        self.BMED_textbrowser.setObjectName("BMED_textbrowser")
        self.gridLayout_7.addWidget(self.BMED_textbrowser, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_NotifyBMED = QtWidgets.QPushButton(self.page_max30001)
        self.pushButton_NotifyBMED.setObjectName("pushButton_NotifyBMED")
        self.verticalLayout_3.addWidget(self.pushButton_NotifyBMED)
        self.pushButton_ConfigBMED = QtWidgets.QPushButton(self.page_max30001)
        self.pushButton_ConfigBMED.setObjectName("pushButton_ConfigBMED")
        self.verticalLayout_3.addWidget(self.pushButton_ConfigBMED)
        self.buttonBMEDdisconnect = QtWidgets.QPushButton(self.page_max30001)
        self.buttonBMEDdisconnect.setObjectName("buttonBMEDdisconnect")
        self.verticalLayout_3.addWidget(self.buttonBMEDdisconnect)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 1, 0, 2, 1)
        self.buttonRecordBMED = QtWidgets.QPushButton(self.page_max30001)
        self.buttonRecordBMED.setObjectName("buttonRecordBMED")
        self.gridLayout_7.addWidget(self.buttonRecordBMED, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_max30001)
        self.page_maxConfig = QtWidgets.QWidget()
        self.page_maxConfig.setObjectName("page_maxConfig")
        self.label_ConfigurationTitle = QtWidgets.QLabel(self.page_maxConfig)
        self.label_ConfigurationTitle.setGeometry(QtCore.QRect(30, 20, 601, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ConfigurationTitle.sizePolicy().hasHeightForWidth())
        self.label_ConfigurationTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ConfigurationTitle.setFont(font)
        self.label_ConfigurationTitle.setObjectName("label_ConfigurationTitle")
        self.pushButton_CfgPort = QtWidgets.QPushButton(self.page_maxConfig)
        self.pushButton_CfgPort.setGeometry(QtCore.QRect(100, 140, 93, 28))
        self.pushButton_CfgPort.setObjectName("pushButton_CfgPort")
        self.textBrowser_CfgOutput = QtWidgets.QTextBrowser(self.page_maxConfig)
        self.textBrowser_CfgOutput.setEnabled(True)
        self.textBrowser_CfgOutput.setGeometry(QtCore.QRect(60, 270, 551, 241))
        self.textBrowser_CfgOutput.setObjectName("textBrowser_CfgOutput")
        self.label_CfgCurrentMode = QtWidgets.QLabel(self.page_maxConfig)
        self.label_CfgCurrentMode.setEnabled(False)
        self.label_CfgCurrentMode.setGeometry(QtCore.QRect(370, 110, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_CfgCurrentMode.setFont(font)
        self.label_CfgCurrentMode.setObjectName("label_CfgCurrentMode")
        self.label_CfgSelectMode = QtWidgets.QLabel(self.page_maxConfig)
        self.label_CfgSelectMode.setEnabled(False)
        self.label_CfgSelectMode.setGeometry(QtCore.QRect(370, 150, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_CfgSelectMode.setFont(font)
        self.label_CfgSelectMode.setObjectName("label_CfgSelectMode")
        self.pushButton_CfgSelectMode = QtWidgets.QPushButton(self.page_maxConfig)
        self.pushButton_CfgSelectMode.setEnabled(False)
        self.pushButton_CfgSelectMode.setGeometry(QtCore.QRect(370, 210, 161, 28))
        self.pushButton_CfgSelectMode.setObjectName("pushButton_CfgSelectMode")
        self.pushButton_CfgEnd = QtWidgets.QPushButton(self.page_maxConfig)
        self.pushButton_CfgEnd.setGeometry(QtCore.QRect(100, 190, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CfgEnd.setFont(font)
        self.pushButton_CfgEnd.setObjectName("pushButton_CfgEnd")
        self.label_CfgPorts = QtWidgets.QLabel(self.page_maxConfig)
        self.label_CfgPorts.setGeometry(QtCore.QRect(70, 110, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_CfgPorts.setFont(font)
        self.label_CfgPorts.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_CfgPorts.setObjectName("label_CfgPorts")
        self.comboBox_CfgPorts = QtWidgets.QComboBox(self.page_maxConfig)
        self.comboBox_CfgPorts.setGeometry(QtCore.QRect(150, 110, 151, 22))
        self.comboBox_CfgPorts.setObjectName("comboBox_CfgPorts")
        self.comboBox_CfgModes = QtWidgets.QComboBox(self.page_maxConfig)
        self.comboBox_CfgModes.setEnabled(False)
        self.comboBox_CfgModes.setGeometry(QtCore.QRect(370, 170, 241, 22))
        self.comboBox_CfgModes.setObjectName("comboBox_CfgModes")
        self.comboBox_CfgModes.addItem("")
        self.comboBox_CfgModes.addItem("")
        self.comboBox_CfgModes.addItem("")
        self.comboBox_CfgModes.addItem("")
        self.comboBox_CfgModes.addItem("")
        self.comboBox_CfgModes.addItem("")
        self.pushButton_CfgRefresh = QtWidgets.QPushButton(self.page_maxConfig)
        self.pushButton_CfgRefresh.setGeometry(QtCore.QRect(200, 140, 93, 28))
        self.pushButton_CfgRefresh.setObjectName("pushButton_CfgRefresh")
        self.stackedWidget.addWidget(self.page_maxConfig)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BLE testing app"))
        self.label_discovered.setText(_translate("MainWindow", "Discovered devices"))
        self.pushButton_clearOut.setText(_translate("MainWindow", "Clear"))
        self.pushButtonScan.setText(_translate("MainWindow", "Scan for devices"))
        self.pushButton_Conn.setText(_translate("MainWindow", "Connect to device"))
        self.label_devinfo.setText(_translate("MainWindow", "Device info (left click for info)"))
        self.label_output.setText(_translate("MainWindow", "Output"))
        self.label_4.setText(_translate("MainWindow", ">>"))
        self.label_Configuration.setText(_translate("MainWindow", "MAX30001 device configuration:"))
        self.pushButton_Configuration.setText(_translate("MainWindow", "Configuration..."))
        self.label_output_2.setText(_translate("MainWindow", "Output"))
        self.label_2.setText(_translate("MainWindow", ">>"))
        self.label_3.setText(_translate("MainWindow", "BLE device charachteristics:"))
        self.label.setText(_translate("MainWindow", "BLE device services:"))
        self.pushButton_clearOut_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.pushButtonService.setText(_translate("MainWindow", "Select service"))
        self.pushButton_Characteristic.setText(_translate("MainWindow", "Select characteristic"))
        self.HRVLabel.setText(_translate("MainWindow", "Heart rate value:"))
        self.pushButtonRecord.setText(_translate("MainWindow", "Start recording"))
        self.pushButtonNotifyHR.setText(_translate("MainWindow", "Pause data tracking"))
        self.buttonHRdisconnect.setText(_translate("MainWindow", "Disconnect from device"))
        self.label_HeartRateBMED.setText(_translate("MainWindow", "Average heart rate: 0"))
        self.label_TrainingZoneBMED.setText(_translate("MainWindow", "Training zone:"))
        self.label_biometricDataBMED.setText(_translate("MainWindow", "Subject biometric data:"))
        self.pushButton_NotifyBMED.setText(_translate("MainWindow", "Pause data tracking"))
        self.pushButton_ConfigBMED.setText(_translate("MainWindow", "Change device mode"))
        self.buttonBMEDdisconnect.setText(_translate("MainWindow", "Disconnect from device"))
        self.buttonRecordBMED.setText(_translate("MainWindow", "Start Recording"))
        self.label_ConfigurationTitle.setText(_translate("MainWindow", "MAX30001 device configuration (connect device via USB)"))
        self.pushButton_CfgPort.setText(_translate("MainWindow", "Open Port"))
        self.label_CfgCurrentMode.setText(_translate("MainWindow", "Current device mode:"))
        self.label_CfgSelectMode.setText(_translate("MainWindow", "Select new device mode"))
        self.pushButton_CfgSelectMode.setText(_translate("MainWindow", "Change to selected"))
        self.pushButton_CfgEnd.setText(_translate("MainWindow", "End configuration"))
        self.label_CfgPorts.setText(_translate("MainWindow", "Port:"))
        self.comboBox_CfgModes.setItemText(0, _translate("MainWindow", "MODE_ECG"))
        self.comboBox_CfgModes.setItemText(1, _translate("MainWindow", "MODE_HR_ECG"))
        self.comboBox_CfgModes.setItemText(2, _translate("MainWindow", "MODE_ICM_ECG"))
        self.comboBox_CfgModes.setItemText(3, _translate("MainWindow", "MODE_COMBINED"))
        self.comboBox_CfgModes.setItemText(4, _translate("MainWindow", "MODE_BIOZ"))
        self.comboBox_CfgModes.setItemText(5, _translate("MainWindow", "MODE_ACCEL"))
        self.pushButton_CfgRefresh.setText(_translate("MainWindow", "Refresh ports"))
from pyqtgraph import PlotWidget
