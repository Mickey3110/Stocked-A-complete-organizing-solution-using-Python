
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date,datetime

conn=sqlite3.connect('stock.db')
curr=conn.cursor()

conn2=sqlite3.connect('revenue.db')
curr2=conn2.cursor()

back=0


class Ui_MainWindow2(object):
    def setup2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 60, 221, 178))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 260, 491, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.inser)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(260, 60, 256, 192))
        self.textEdit_9.setObjectName("textBrowser")
        self.textEdit_9.setReadOnly(True)      

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        
        font.setWeight(75)
        self.textEdit_9.setFont(font)
 
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("Name")
        self.label_2.setText("CP")
        self.label_3.setText("Quantity")
        self.label_4.setText("Mfg")
        self.label_5.setText("Expiry")
        self.label_6.setText("SP")
        self.pushButton_2.setText("Add")
        self.pushButton.setText("Main Menu")

        

        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
    def inser(self):
        print(self.lineEdit.text())
        print(int(self.lineEdit_2.text()))
        print(int(self.lineEdit_3.text()))
        print(self.dateEdit.date().toPyDate())
        print(self.dateEdit_2.date().toPyDate())
        print(int(self.lineEdit_6.text()))
        
        
        curr.execute('Insert into stock values(?,?,?,?,?,?)',(self.lineEdit.text(),int(self.lineEdit_2.text()),int(self.lineEdit_3.text()),self.dateEdit.date().toPyDate(),self.dateEdit_2.date().toPyDate(),int(self.lineEdit_6.text())))
        conn.commit()
        a=0
        r1=date.today().strftime("%Y/%m/%d")
        curr2.execute('Insert into revenue values(?,?,?,?,?,?)',(self.lineEdit.text(),int(self.lineEdit_2.text()),int(self.lineEdit_6.text()),a,a,r1))
        conn2.commit()
        a= "insert sucessful"+"\nName: "+self.lineEdit.text()+"\nCP: "+self.lineEdit_2.text()+"\nQuantity:"+self.lineEdit_2.text()+"\nMFG:"+str(self.dateEdit.date().toPyDate())+"\nExpiry:"+str(self.dateEdit_2.date().toPyDate())+"\nSP: "+self.lineEdit_6.text()
        print(a)
        self.textEdit_9.setText(a)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.dateEdit.clear()
        self.dateEdit_2.clear()
        self.lineEdit_6.clear()
        
         
         
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setup2(MainWindow2)
    MainWindow2.show()
    
    sys.exit(app.exec_())
