
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime,date

conn1=sqlite3.connect('stock.db')
curr1=conn1.cursor()

conn2=sqlite3.connect('customer.db')
curr2=conn2.cursor()

conn3=sqlite3.connect('revenue.db')
curr3=conn3.cursor()

class Ui_MainWindow4(object):
    def setup4(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 281, 301))
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
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.listView = QtWidgets.QListView(self.formLayoutWidget)
        self.listView.setObjectName("listView")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.listView)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 350, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(320, 60, 241, 241))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 40, 191, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 310, 241, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 5, 271, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 390, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.totall=0
        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("Customer name")
        self.label_2.setText("Address")
        self.label_3.setText("Phone no.:")
        self.label_8.setText("id")
        self.label_4.setText("Select item:")
        self.label_5.setText("Quantity")
        self.pushButton.setText("Add selected item to bill")
        self.pushButton_2.setText("Bill for next customer")
        self.label_6.setText("Items in the bill")
        self.label_7.setText("Billing")
        self.loadList()
        self.d=""
        self.pushButton.clicked.connect(self.transfer)
        self.pushButton_2.clicked.connect(self.cle)
        self.z=""
    def loadList(self):
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        curr1.execute('select item FROM stock')
        rows= curr1.fetchall()
        conn1.commit()
        entries=[]
        
        for row in rows:
            entries.append(row[0])
        for i in entries:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        self.listView.clicked.connect(self.giveName)
        
    def giveName(self):
        itms = self.listView.selectedIndexes()
        print(itms)
        for x in itms:
            self.d=str(x.data())
            
        print(self.d)
        

    def transfer(self):
        self.quantity=int(self.lineEdit_4.text())
        self.z+= self.d + "\t" + str(self.quantity)+"\n"
        curr1.execute('Update stock set quantity = quantity- ? where item = ?' ,(self.quantity,self.d,))
        conn1.commit()
        
        p=self.lineEdit.text()
        q=self.lineEdit_2.text()
        r=self.lineEdit_3.text()
        s=self.lineEdit_5.text()
        print(self.z)
        self.textEdit.setText(self.z)
        if self.totall==0:
            print(s)
            curr2.execute('select ID from customer where ID=?',(s,))
            ro=curr2.fetchall()
            conn2.commit()
            print(ro)
            if len(ro)==0:
                
               print(p)
               print(q)
               print(r)
               curr2.execute('insert into customer values(?,?,?,?)' ,(s,p,q,r,))
               conn2.commit()
               print('A')
        r1=date.today().strftime("%Y/%m/%d")
        curr2.execute('insert into customer_bought values(?,?,?,?,?)',(self.lineEdit.text(),self.d,self.quantity,r1,s,))
        conn2.commit()
        self.profit()
        self.total()
        
        
    def profit(self):
        curr1.execute('select sp-cp from stock where item=?',(self.d,))
        s=curr1.fetchall()
        conn1.commit()
        self.profi = 0   
        for s1 in s:
            self.profi += s1[0] * self.quantity
        print(self.profi)
        print(self.profi)
        curr3.execute('Update revenue set profit = profit + ?, quantity= quantity + ? where item = ?',(self.profi,self.quantity,self.d,))
        conn3.commit()
        r1=date.today().strftime("%Y/%m/%d")
        curr3.execute('Insert into daily values(?,?,?)',(self.d,self.quantity,r1))
        conn3.commit()
    def total(self):
        curr1.execute('select sp from stock where item=?',(self.d,))
        s=curr1.fetchall()
        conn1.commit()
        for s1 in s:
            self.totall += s1[0]* self.quantity
        print(self.totall)
        o=str(self.totall)
        o="total without gst : "+o
        
        p=round(self.totall * 1.1,2)
        p=str(p)
        p="\n Total with gst :" +p
        p=o+p
        self.textEdit_2.setText(p)

    def cle(self):
        print('A')
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        print('A')
        self.z=""
        self.totall=0
        self.textEdit.setText(self.z)
        print('A')
        self.textEdit_2.setText(self.z)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setup4(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
