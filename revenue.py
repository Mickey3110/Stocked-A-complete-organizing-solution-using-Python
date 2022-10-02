from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date,datetime

conn3= sqlite3.connect('revenue.db')
curr3 = conn3.cursor()

class Ui_MainWindow7(object):
    def setup7(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 130, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 40, 241, 71))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 170, 171, 101))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(230, 170, 171, 101))
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("Stats for the day")
        self.label_2.setText("Stats for the month")
        self.label_3.setText("Stats for the year")
        self.tod()
        self.mot()
        self.yea()
    def tod(self):
        r1=date.today().strftime("%Y/%m/%d")
        curr3.execute('select a.item, a.CP,a.SP,a.profit,b.quantity,b.sold_date from revenue a join daily b on a.item=b.item where b.sold_date=?',(r1,))
        rows=curr3.fetchall()
        conn3.commit()
        quant=0
        profit=0
        print(rows)
        for row in rows:
            quant+=row[4]
            profit+=row[3]
        z="Total items sold today: "+str(quant)+"\nTotal profit today: Rs. "+str(profit)
        print(z)
        self.textEdit.setText(z)
    def mot(self):
        r1=date.today().strftime("%Y/%m/%d")
        r=r1[:8]
        r=r+"__"
        print(r)
        curr3.execute('select a.item, a.CP,a.SP,a.profit,b.quantity,b.sold_date from revenue a join daily b on a.item=b.item where b.sold_date like ?',(r,))
        rows=curr3.fetchall()
        conn3.commit()
        quant=0
        profit=0
        print(rows)
        for row in rows:
            quant+=row[4]
            profit+=row[3]
        z1="Total items sold this month: "+str(quant)+"\nTotal profit this month: Rs. "+str(profit)
        print(z1)
        self.textEdit_2.setText(z1)
        
    def yea(self):
        r1=date.today().strftime("%Y/%m/%d")
        r=r1[:5]
        r=r+"__/__"
        print(r)
        curr3.execute('select a.item, a.CP,a.SP,a.profit,b.quantity,b.sold_date from revenue a join daily b on a.item=b.item where b.sold_date like ?',(r,))
        rows=curr3.fetchall()
        conn3.commit()
        quant=0
        profit=0
        print(rows)
        for row in rows:
            quant+=row[4]
            profit+=row[3]
        z2="Total items sold this year: "+str(quant)+"\nTotal profit this year: Rs. "+str(profit)
        print(z2)
        self.textEdit_3.setText(z2)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow7()
    ui.setup7(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
