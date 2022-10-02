
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn=sqlite3.connect('stock.db')
curr=conn.cursor()


class Ui_MainWindow6(object):
    def setup6(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(60, 60, 361, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 371, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("STOCK KEEPER")
        self.z="item name \t Quantity"
        self.textEdit = QtWidgets.QTextEdit()
        self.scrollArea.setWidget(self.textEdit)
        self.showStock()

    def showStock(self):
        curr.execute('Select item,quantity from stock')
        rows=curr.fetchall()
        conn.commit()
        for row in rows:
            self.z += "\n"+row[0] +"\t"+str(row[1])
        self.textEdit.setText(self.z)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow6()
    ui.setup6(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
