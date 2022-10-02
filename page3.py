
from PyQt5 import QtCore, QtGui, QtWidgets
from addstock import Ui_MainWindow2
from expiry1 import Ui_MainWindow3
from bill import Ui_MainWindow4
from search import Ui_MainWindow5
from skeeper import Ui_MainWindow6
from revenue import Ui_MainWindow7
from trend import Ui_MainWindow8
from employee import Ui_MainWindow9

class Ui_MainWindowMain(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 171, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 140, 171, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 351, 41))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("MainWindow")
        self.pushButton_2.setText("Add Stock")
        self.pushButton_4.setText("Check expiry")
        self.pushButton_3.setText("Bill creation")
        self.pushButton.setText("Check Stock")
        self.pushButton_7.setText("Search")
        self.pushButton_8.setText("Employees")
        self.pushButton_6.setText("Trending")
        self.pushButton_5.setText("Revenue")
        self.lineEdit.setText("Choose the options from below")

        
        
        self.pushButton_2.clicked.connect(self.onClickAddStock)
        self.pushButton_4.clicked.connect(self.onClickExpiry)
        self.pushButton_3.clicked.connect(self.onClickBill)
        self.pushButton_7.clicked.connect(self.onClickSearch)
        self.pushButton_8.clicked.connect(self.onClickEmployee)
        self.pushButton.clicked.connect(self.onClickStock)
        self.pushButton_5.clicked.connect(self.onClickRevenue)
        self.pushButton_6.clicked.connect(self.onClickTrend)
        
    def onClickAddStock(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        
        self.ui.setup2(self.Window2)
        self.Window2.show()

    def onClickExpiry(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow3()
        
        self.ui.setup3(self.Window2)
        self.Window2.show()
        
        
    def onClickBill(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow4()
        
        self.ui.setup4(self.Window2)
        self.Window2.show()
        
    def onClickSearch(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow5()
        
        self.ui.setup5(self.Window2)
        self.Window2.show()
        
    def onClickStock(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow6()
        
        self.ui.setup6(self.Window2)
        self.Window2.show()  

    def onClickRevenue(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow7()
        
        self.ui.setup7(self.Window2)
        self.Window2.show()

    def onClickTrend(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow8()
        
        self.ui.setup8(self.Window2)
        self.Window2.show()

    def onClickEmployee(self):
        self.Window2=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow9()
        
        self.ui.setup9(self.Window2)
        self.Window2.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowMain()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
