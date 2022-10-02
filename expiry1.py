from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime,date

conn=sqlite3.connect('stock.db')
curr=conn.cursor()


class Ui_MainWindow3(object):
    def setup3(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 262, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 70, 181, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(270, 70, 181, 171))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 179, 169))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setUnderline(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
  
        MainWindow.setWindowTitle("MainWindow")
        self.pushButton.setText("Remove Expired items")
        self.pushButton.clicked.connect(self.removeExpired)
        self.lineEdit.setText("Put the expiring items on sale!!!")
        self.lineEdit_2.setText("Remove the expired items")
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit_2 = QtWidgets.QTextEdit()
        
        self.scrollArea.setWidget(self.textEdit)
        self.scrollArea_2.setWidget(self.textEdit_2)
        MainWindow.setWindowTitle("MainWindow")
        
        self.searchExpired()
        self.searchExpiring()
    def searchExpired(self):
            k1=0
            print(k1)
            curr.execute('select item,expiry FROM stock')
            rows= curr.fetchall()
            z='Expired Items \n Item name      date'
            self.textEdit.setText(z)
            for row in rows:
                x=row[1]
                y=date.today()
                date_object = datetime.strptime(x, '%Y-%m-%d').date()
                if (date_object<y):
                    k1+=1
                    z+='\n'
                    z+=row[0]+ "       " +str(date_object)
            if k1!=0:   
             self.textEdit.setText(z)
            else:
              self.textEdit.setText("no expired items")
    def searchExpiring(self):
        k2=0
        curr.execute('select item,expiry FROM stock')
        rows= curr.fetchall()
        conn.commit()
        p='Expiring Items \n Item name      date'
        self.textEdit_2.setText(p)
        for row in rows:
            x=row[1]
            y=date.today()
            print(row[0])
            
            date_object = datetime.strptime(x, '%Y-%m-%d').date()
            if ((date_object-y).days<30 and (date_object-y).days>0):
                k2+=1
                p+='\n'
                p+=row[0]+ "       " +str(date_object)
        if k2!=0:
            self.textEdit_2.setText(p)
        else:
            self.textEdit_2.setText("No items expiring within a month")
    def removeExpired(self):
        curr.execute('DELETE FROM stock where expiry<date(\'now\')')
        conn.commit()
        z='expired items removed'
        
        self.searchExpired()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setup3(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
