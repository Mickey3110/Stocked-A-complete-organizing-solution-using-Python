
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn3=sqlite3.connect('revenue.db')
curr3=conn3.cursor()

class Ui_MainWindow8(object):
    def setup8(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 50, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 190, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("Most sold product recently")
        self.label_2.setText("Least sold product recently")
        self.most()
        self.least()
    def most(self):
        curr3.execute('Select item from revenue order by quantity desc')
        rows=curr3.fetchall()
        conn3.commit()
        y=""
        for z in range(0,3):
            y+=str(z+1)+"."+rows[z][0]+"\n"
        self.textEdit.setText(y)

    def least(self):
        curr3.execute('Select item from revenue order by quantity')
        rows=curr3.fetchall()
        conn3.commit()
        y=""
        for z in range(0,3):
            y+=str(z+1)+"."+rows[z][0]+"\n"
        self.textEdit_2.setText(y)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow8()
    ui.setup8(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
