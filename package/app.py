import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt6.QtCore import QByteArray, QDate, QIODevice, QTime, QDateTime, QFile
from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.QtBluetooth import QBluetoothUuid, QLowEnergyService
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6.QtGui import QIcon

from pyqtgraph import PlotWidget, plot, mkPen
from package.gui import Ui_MainWindow
from package.ble_utils.Scan import BLE_Scanner
from package.ble_utils.Controller import BLE_Controller

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.ble_scanner = BLE_Scanner()
        self.ble_controller = BLE_Controller()

        self.pushButton_Conn.setEnabled(False)  ##initially not enabled, only after device selection
        self.pushButtonService.setEnabled(False) ## initialy not enabled, only after service selection
        self.pushButton_Characteristic.setEnabled(False)   #same
        

    #Event signals
        self.listWidget.itemClicked.connect(self.selectedFromList)
        self.listWidget_2.itemClicked.connect(self.serviceClicked)
        self.listWidget_characteristics.itemClicked.connect(self.characteristicClicked)
        self.pushButton_clearOut.clicked.connect(self.clearOutput)
        self.pushButton_clearOut_2.clicked.connect(self.clearOutput2)
        self.pushButton_Disconnect.clicked.connect(self.handleButtonDisconnect)
        self.pushButtonService.clicked.connect(self.handleButtonService)
        self.pushButton_Characteristic.clicked.connect(self.handleButtonChar)
        self.buttonRecordBMED.clicked.connect(self.handleButtonRecordBMED)
        self.buttonBMEDdisconnect.clicked.connect(self.handleButtonDisconnect)
        self.buttonHRdisconnect.clicked.connect(self.handleButtonDisconnect)
        self.pushButton_Configuration.clicked.connect(self.handleButtonConfiguration)
        # Max30001 device configuration signals
        
        #BLE Scanner events
        self.pushButtonScan.clicked.connect(self.handleButtonScan)
        self.ble_scanner.discoveryAgent.finished.connect(self.updateList)
        #self.ble_scanner.discoveryAgent.error.connect(self.errorHandle)
        self.ble_scanner.scannerOutputMessage.connect(self.updateOutput)
        #BLE Controller events
        self.ble_controller.controllerOutputMessage.connect(self.updateOutput2)
        self.pushButton_Conn.clicked.connect(self.handleButtonConn)
        self.ble_controller.controllerConnected.connect(self.handleDeviceConnected)
        self.ble_controller.servicesFound.connect(self.handleServicesFound)
        #BLE Service events
        self.ble_controller.serviceOpened.connect(self.handleOpenedService)


########## DEVICES PAGE ###############################

    def handleButtonScan(self):
        self.pushButton_Conn.setEnabled(False)
        print("Scan clicked!")
        self.textBrowser.clear()
        self.ble_scanner.scanDevices()

    def updateList(self):
        self.listWidget.clear()
        
        ##print("Update run")
        for obj in self.ble_scanner.discoveryAgent.discoveredDevices():
            self.item2add = QtWidgets.QListWidgetItem()
            self.item2add.setText(obj.name())
            self.item2add.setData(QtCore.Qt.ItemDataRole.UserRole, obj)
                        
            ##print("BTDevice", obj.name())      
            
            self.item2add.setToolTip(obj.name())
            self.listWidget.addItem(self.item2add)
        
        self.textBrowser_2.append(">>Scan finished\n")
    
    #Device clicked in list view
    def selectedFromList(self, itemC):
        self.pushButton_Conn.setEnabled(True)
        
        self.deviceInfo = itemC.data(QtCore.Qt.ItemDataRole.UserRole)

        ##print("self.devIfno", self.deviceInfo)  # PyQt6.QtBluetooth.QBluetoothDeviceInfo
        ##print("self.itemC::", itemC)  # PyQt6.QtWidgets.QListWidgetItem
        
        if(self.deviceInfo.coreConfigurations() == 1):
            self.devType = "Bluetooth low energy device"
        elif (self.deviceInfo.coreConfigurations() == 2):
            self.devType = "Bluetooth standard device"
        else:
            self.devType = "Bluetooth standard and low energy device"
        
        #print("{0}\n".format(self.deviceInfo.address().toString()))
        self.textBrowser.setText("Device name: " + self.deviceInfo.name() +
                                 "\nDevice type: " + self.devType +
                                 "\nMAC address: " + self.deviceInfo.address().toString() +
                                 "\nDevice UUID: " + self.deviceInfo.deviceUuid().toString() + '\n')

    #Connects to device selected in listview
    def handleButtonConn(self):
        self.ble_controller.connectDevice(self.listWidget.currentItem().data(QtCore.Qt.ItemDataRole.DisplayRole))

    def handleButtonConfiguration(self):
        self.stackedWidget.setCurrentIndex(4)  #switch to "Configuration page"
        self.setupConfigurationPage()


################### SERVICES PAGE ###############################

    #Disconnects from current device
    def handleButtonDisconnect(self):
        self.stackedWidget.setCurrentIndex(0)
        self.ble_controller.disconnect()
        self.textBrowser_2.append(">>Disconnected from device\n")   #output page 1
        self.listWidget.clear()     #found devices on page 1
        self.textBrowser.clear()    #device info on page 1
        self.listWidget_2.clear()   #services list on page 2
        self.listWidget_characteristics.clear()  #page 2 char browser
        self.textBrowser_3.clear()  ##output on page 2
        self.pushButton_Conn.setEnabled(False)
        self.pushButtonService.setEnabled(False)
        self.pushButton_Characteristic.setEnabled(False)

    #Called when succesfully connected to device
    def handleDeviceConnected(self):
        print("Changing page\n")
        self.stackedWidget.setCurrentIndex(1)  #switch to "services page"
        self.textBrowser_3.append(">>Connected to device\n")
        #self.ble_serviceAgent.scan_services(self.ble_controller.ble_device.address())

    #Adds discovered BLE services to list view
    def handleServicesFound(self):
        for servicesUids in self.ble_controller.controller.services():
            self.ble_service_uuid = QBluetoothUuid(servicesUids)
            print(self.ble_service_uuid.toString())
            self.foundService = self.ble_controller.controller.createServiceObject(self.ble_service_uuid)
            if self.foundService == None:
                print("Not created")
            self.itemService = QtWidgets.QListWidgetItem()
            self.itemService.setText(self.foundService.serviceName())
            self.itemService.setData(QtCore.Qt.UserRole, self.ble_service_uuid)
            self.listWidget_2.addItem(self.itemService)

    def serviceClicked(self):
        self.pushButtonService.setEnabled(True)

    #Selected service to be discovered, calls readService(uuid)
    def handleButtonService(self):
        #self.listWidget_characteristics.clear()
        self.pushButton_Characteristic.setEnabled(False)
        self.ble_controller.readService(self.listWidget_2.currentItem().data(QtCore.Qt.UserRole))

    # When service is succesfully opened, we open appropriate page
    #   CURRENTLY IMPLEMENTED SPECIAL SERVICE PAGES:
    #       - HEART RATE SERVICE
    #       - Cable replacement service with custom Uuid '0000fe60-cc7a-482a-984a-7f2ed5b3e58f'
    #
    # if not special service is selected, we simply list service characteristics on same page
    def handleOpenedService(self):
        self.listWidget_characteristics.clear()
        # IF Heart Rate Service Selected then open HR Page
        if (self.ble_controller.openedService.serviceUuid() == QBluetoothUuid(QBluetoothUuid.HeartRate)):
            self.stackedWidget.setCurrentIndex(2)       # switch to HEART RATE Page
            self.setupHeartRatePage()

        ##WIP
        elif (self.ble_controller.openedService.serviceUuid() == QBluetoothUuid("{0000fe60-cc7a-482a-984a-7f2ed5b3e58f}")):
            self.stackedWidget.setCurrentIndex(3)      #SWITCH to BIOMED Page
            self.setupCRS_customPage()
            
        #if no special service selected, stay on current page view
        else:
            for obj in self.ble_controller.openedService.characteristics():
                self.itemChar = QtWidgets.QListWidgetItem()
                if (obj.name() == ""):
                    self.itemChar.setText("Unknown characteristic")
                else:
                    self.itemChar.setText(obj.name())
                self.itemChar.setData(QtCore.Qt.UserRole, obj)
                self.listWidget_characteristics.addItem(self.itemChar)

    def characteristicClicked(self):
        self.pushButton_Characteristic.setEnabled(True)

    def handleButtonChar(self):
        self.karakteristika = self.listWidget_characteristics.currentItem().data(QtCore.Qt.UserRole)

        self.tekst = self.karakteristika.value().data().decode()                #Ispis prve vrijednosti karakteristike odabrane
        self.textBrowser_3.append("Received: {0}".format(self.tekst))

        self.type = QBluetoothUuid(QBluetoothUuid.ClientCharacteristicConfiguration)
        self.descript = self.karakteristika.descriptor(self.type)

        self.array = QByteArray(b'\x01\x00')        #turn on NOTIFY for characteristic

        self.ble_controller.openedService.characteristicChanged.connect(self.updateVal)
        self.ble_controller.openedService.writeDescriptor(self.descript, self.array)    #turn on NOTIFY
    
    def updateVal(self, Charac, newVal):
        self.val = QByteArray()
        self.val = newVal

        #self.strng = int(self.val[1].hex(), 16)
        self.strng = self.val.data().decode()           #decode bytes to string
        #print(self.strng)
        self.textBrowser_3.append("Received value : {0}".format(self.strng))


################# HEART RATE SERVICE PAGE #####################
    def setupHeartRatePage(self):
        #graph setup
        self.graph_heartrate.setBackground("w")
        self.HRvaluesArray = [0]         #Heart rate values for plotting
        self.timevaluesArray = [0]           #Time values for plotting
        self.start_time = time.perf_counter()  #Start collecting time value
        pen = mkPen(color=(255, 0, 0))
        self.data_line =  self.graph_heartrate.plot(self.timevaluesArray, self.HRvaluesArray, pen=pen)

        # Subscribe to notification for Heart Rate value changes via descriptor writing
        self.heartRateMeasurChar = self.ble_controller.openedService.characteristic(QBluetoothUuid(QBluetoothUuid.HeartRateMeasurement))
        if (self.heartRateMeasurChar.isValid() == False):
            print("ERR: Cannot read heart rate measurement characteristic\n")

        self.HRCharCfg = QBluetoothUuid(QBluetoothUuid.ClientCharacteristicConfiguration)
        self.HRdescript = self.heartRateMeasurChar.descriptor(self.HRCharCfg)
        if (self.HRdescript.isValid() == False):
            print("ERR: Cannot create notification for HeartRate value\n")

        self.array = QByteArray(b'\x01\x00')        #turn on NOTIFY for characteristic

        self.ble_controller.openedService.characteristicChanged.connect(self.handleHRValueChanged)
        self.ble_controller.openedService.writeDescriptor(self.HRdescript, self.array)    #turn on NOTIFY

    #called when HR value changed
    def handleHRValueChanged(self, Charac, newVal):
        self.HeartRateValue = QByteArray()
        self.HeartRateValue = newVal
        self.HeartRateValueString = int(self.HeartRateValue[1].hex(), 16)

        self.lcdHeartRate.display(self.HeartRateValueString)     #update lcd display
        self.updateHRGraph(self.HeartRateValueString)              # plot new values

    #UPDATE graph values
    def updateHRGraph(self, Yvalue):
        if(len(self.HRvaluesArray) > 200):
            self.HRvaluesArray = self.HRvaluesArray[1:]         #remove first elements after 200 inputs
            self.timevaluesArray = self.timevaluesArray[1:]

        self.HRvaluesArray.append(Yvalue)

        self.elapsed_time = time.perf_counter() - self.start_time
        self.timevaluesArray.append(self.elapsed_time)

        self.data_line.setData(self.timevaluesArray, self.HRvaluesArray)

################# Custom Cable replacement service PAGE #####################
    def setupCRS_customPage(self):
        self.recordingActive = False
        self.elapsed_time = 0
        self.isICMReceived = False
        self.currentHeartRate = 0
        self.maxHeartRate = 100
        #graph setup
        self.max30001_graph.setBackground('w')
        self.RXvaluesArray = [0.0]         #Recieved values for plotting
        self.timevaluesArray = [0.0]           #Time values for plotting
        self.start_time = time.perf_counter()  #Start collecting time value
        pen = mkPen(color=(255, 0, 0))
        self.data_line =  self.max30001_graph.plot(self.timevaluesArray, self.RXvaluesArray, pen=pen)

        # Subscribe to notification for CRS RX value changes via descriptor writing
        self.RXMeasurChar = self.ble_controller.openedService.characteristic(QBluetoothUuid("{0000fe62-8e22-4541-9d4c-21edae82ed19}"))        #uuid RX karakteristike
        if (self.RXMeasurChar.isValid() == False):
            print("ERR: Cannot read RX characteristic\n")

        self.RXCharCfg = QBluetoothUuid(QBluetoothUuid.ClientCharacteristicConfiguration)
        self.RXdescript = self.RXMeasurChar.descriptor(self.RXCharCfg)
        if (self.RXdescript.isValid() == False):
            print("ERR: Cannot create notification for CRS RX value\n")

        self.array = QByteArray(b'\x01\x00')        #turn on NOTIFY for characteristic

        self.ble_controller.openedService.characteristicChanged.connect(self.handleRXValueChanged)
        self.ble_controller.openedService.writeDescriptor(self.RXdescript, self.array)    #turn on NOTIFY

    #called when RX value changed
    def handleRXValueChanged(self, Charac, newVal):
        if (Charac.uuid() == QBluetoothUuid("{0000fe62-8e22-4541-9d4c-21edae82ed19}")):
            self.RXValue = QByteArray()
            self.RXValue = newVal
            self.RXValueString = self.RXValue.data().decode()

            self.elapsed_time = time.perf_counter() - self.start_time

            if (self.RXValueString[0:2] == "HR"):
                #print("Heart rate is " + self.RXValueString[2:])
                if (self.elapsed_time > 30.0):
                    self.currentHeartRate = int(round(float(self.RXValueString[5:])))    # Data format is "HR = %f"
                    self.label_HeartRateBMED.setText("Average heart rate: " + str(self.currentHeartRate))
                    self.updateTrainingZone(self.currentHeartRate)
            else:
                self.RXValueFloat = float(self.RXValueString)
                self.updateBMEDGraph(self.elapsed_time, self.RXValueFloat)              # plot new values

            if(self.recordingActive == True):
                self.updateLog(self.elapsed_time, self.RXValueString)

            

            # if (self.RXValueString == "START_ICM\r\n"):
            #     self.isICMReceived = True
            #     self.elapsed_time = time.perf_counter() - self.start_time
            #     self.ICMstringToLog = str(self.elapsed_time)
            #     return
            # elif((self.RXValueString == "END_ICM\r\n")):
            #     self.isICMReceived = False
            #     self.ICMstringToLog = self.ICMstringToLog + "\r\n"
            #     #self.updateLog(self.ICMstringToLog)
            #     return
            # else:
            #     if (self.isICMReceived == True):
            #         self.ICMstringToLog = self.ICMstringToLog + ";" + self.RXValueString

            #     else:                                                       #Data is not ICM
                    
    def updateTrainingZone(self, CurrentHRValueInt):
        HRtoMaxHR = CurrentHRValueInt/float(self.maxHeartRate)
        print(str(HRtoMaxHR))

        if (HRtoMaxHR < 0.65):
            #Training zone 1
            self.label_TrainingZoneBMED.setText("Training zone: ZONE 1")
            
        elif (HRtoMaxHR >= 0.65 and HRtoMaxHR < 0.75):
            
            #Training zone 2
            self.label_TrainingZoneBMED.setText("Training zone: ZONE 2")
            
        elif (HRtoMaxHR >= 0.75 and HRtoMaxHR < 0.82):
            #Training zone 3
            self.label_TrainingZoneBMED.setText("Training zone: ZONE 3")
            
        elif (HRtoMaxHR >= 0.82 and HRtoMaxHR < 0.89):
            
            #Training zone 4
            self.label_TrainingZoneBMED.setText("Training zone: ZONE 4")
            
        elif (HRtoMaxHR >= 0.89 and HRtoMaxHR < 0.94):
            
            #Training zone 5
            self.label_TrainingZoneBMED.setText("Training zone: ZONE 5")
            
        elif (HRtoMaxHR >= 0.94):
            
            #Training zone 6
            self.label_TrainingZoneBMED.setText("Training zone: ZONE 6")
            
        else:
            
            #Do nothing
            print("ERROR - shouldn't enter here\n")
            
        

    #UPDATE graph values
    def updateBMEDGraph(self, XValue, Yvalue):
        if(len(self.RXvaluesArray) > 700):
            self.RXvaluesArray = self.RXvaluesArray[1:]         #remove first elements after 200 inputs
            self.timevaluesArray = self.timevaluesArray[1:]

        self.RXvaluesArray.append(Yvalue)
        
        self.timevaluesArray.append(XValue)

        self.data_line.setData(self.timevaluesArray, self.RXvaluesArray)


    def updateLog(self,XDataToLog, YDataToLog):
        self.RxStringValue = YDataToLog
        self.TimeValue = XDataToLog

        self.BMED_textbrowser.append(str(self.TimeValue) + ";" + self.RxStringValue)


    def handleButtonRecordBMED(self):
        if (self.recordingActive == False):
            self.buttonRecordBMED.setText("Stop Recording")
            #write to text browser
            self.BMED_textbrowser.append("Log started on " + QDateTime.currentDateTime().toString())
            self.recordingActive = True

        else:
            self.recordingActive = False
            self.buttonRecordBMED.setText("Start Recording")

            self.saveToFile(self.BMED_textbrowser.toPlainText())
            # self.fileSettings = QFileDialog.getSaveFileName()
            # self.fileName = self.fileSettings[0]
            # print(self.fileName)
            # self.file = QFile(self.fileName)
            # self.textout = self.BMED_textbrowser.toPlainText()
            # if self.file.open(QtCore.QIODevice.ReadWrite):
            #     QtCore.QTextStream(self.file) << self.textout
            # else:
            #     QtWidgets.QMessageBox.information(self.tempwizardPage, 'Unable to open file', file.errorString())
            # self.file.close()
            #create file and copy content from text browser

        #change to stop recording


################### MAX30001 DEVICE CONFIGURATION PAGE ###################
    def setupConfigurationPage(self):
        self.pushButton_CfgRefresh.clicked.connect(self.availablePortsRefreshList)
        self.pushButton_CfgEnd.clicked.connect(self.handleButtonExitConfig)
        self.pushButton_CfgPort.clicked.connect(self.handleButtonOpenPort)
        self.pushButton_CfgSelectMode.clicked.connect(self.handleButtonCfgSelectMode)

        self.availablePortsRefreshList()




    def availablePortsRefreshList(self):
        self.AvailablePortsList = QSerialPortInfo.availablePorts()
        for obj in self.AvailablePortsList:
            self.comboBox_CfgPorts.addItem(obj.portName(), obj)

    def handleButtonOpenPort(self):
        self.serialPort = QSerialPort(
            self.comboBox_CfgPorts.currentData(),
            None
        )
        self.serialPort.setBaudRate(QSerialPort.Baud115200)
        self.serialPort.setParity(QSerialPort.NoParity)
        self.serialPort.setFlowControl(QSerialPort.NoFlowControl)
        self.serialPort.setStopBits(QSerialPort.OneStop)
        self.serialPort.setDataBits(QSerialPort.Data8)

        self.serialPort.readyRead.connect(self.handleSerialReceiveData)

        if (self.serialPort.open(QIODevice.ReadWrite) == True):
            self.label_CfgCurrentMode.setEnabled(True)
            self.label_CfgSelectMode.setEnabled(True)
            self.comboBox_CfgModes.setEnabled(True)
            self.pushButton_CfgSelectMode.setEnabled(True)

    def handleButtonCfgSelectMode(self):
        self.serialPort.writeData(self.comboBox_CfgModes.currentText().encode())

    def handleSerialReceiveData(self):
        self.textBrowser_CfgOutput.append(self.serialPort.readAll().data().decode())

    def handleButtonExitConfig(self):
        self.label_CfgCurrentMode.setEnabled(False)
        self.label_CfgSelectMode.setEnabled(False)
        self.comboBox_CfgModes.setEnabled(False)
        self.pushButton_CfgSelectMode.setEnabled(False)
        self.textBrowser_CfgOutput.clear()
        self.stackedWidget.setCurrentIndex(0)  #switch to "Devices page"
        self.serialPort.close()
        del(self.serialPort)


############ SAVE TEXT TO FILE ###########################################

    def saveToFile(self, text):
        self.textout = text

        self.fileSettings = QFileDialog.getSaveFileName()
        self.fileName = self.fileSettings[0]
        print(self.fileName)
        self.file = QFile(self.fileName)

        if self.file.open(QtCore.QIODevice.ReadWrite):
            QtCore.QTextStream(self.file) << self.textout
        else:
            QtWidgets.QMessageBox.information(self.tempwizardPage, 'Unable to open file', file.errorString())
        self.file.close()
        
############ DISCONNECT FROM DEVICE WHEN SERVICE IS OPENED ###############

    def handleServiceDisconnectButton(self):
        print("A")



###### SOME OUTPUTS AND ERROR HANDLE #####################

    def updateOutput(self, message):
        self.textBrowser_2.append(message)

    def clearOutput(self):
        self.textBrowser_2.clear()

    def updateOutput2(self, message):
        self.textBrowser_3.append(message)

    def clearOutput2(self):
        self.textBrowser_3.clear()

    def errorHandle(self, errMessage):
        print("Error handle\n")                 #debug
        print("{0}".format(errMessage.toString()))  #debug
        self.textBrowser_2.append(">>ERROR\n")



############## RUN APP ####################

def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()