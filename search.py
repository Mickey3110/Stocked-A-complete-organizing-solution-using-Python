from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn1=sqlite3.connect('stock.db')
curr1=conn1.cursor()



conn3=sqlite3.connect('customer.db')
curr3=conn3.cursor()

class Ui_MainWindow5(object):
    def setup5(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, -1, 471, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(26, 12, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 90, 160, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(270, 90, 161, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(270, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 90, 70, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 120, 70, 17))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 150, 70, 17))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 110, 191, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 110, 70, 17))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(280, 110, 151, 171))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 149, 169))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(290, 90, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(40, 160, 66, 20))
        self.label_10.setObjectName("label_10")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 160, 70, 17))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.tabWidget.setCurrentIndex(1)
        MainWindow.setWindowTitle("MainWindow")
        self.label.setText("Search for an item by any of the options")
        self.label_2.setText("Name")
        self.label_3.setText("CP")
        self.label_4.setText("SP")
        self.label_5.setText("Results")
        self.pushButton.setText( "search")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),"Item")
        self.label_6.setText("Search  for an customer")
        self.label_7.setText("Name")
        self.label_8.setText("shopped date")
        self.pushButton_2.setText("Search")
        self.label_9.setText("results")
        self.label_10.setText("Id")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),"Customer")

        self.textEdit = QtWidgets.QTextEdit()
        self.scrollArea.setWidget(self.textEdit)

        self.textEdit_2 = QtWidgets.QTextEdit()
        self.scrollArea_2.setWidget(self.textEdit_2)
        self.pushButton.clicked.connect(self.search1)
        self.pushButton_2.clicked.connect(self.search2)
        
    def search1(self):
        if(self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked()):
            k=""
            a=int(self.lineEdit_2.text())
            b=int(self.lineEdit_3.text())
            curr1.execute('select * from stock where item = ? and CP=? and SP=? and Id=?',(self.lineEdit.text(),a,b,))
            rows=curr1.fetchall()
            conn1.commit()
            
            for row in rows:
                k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"
            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k
            self.textEdit.setText(k)

        elif(self.checkBox.isChecked() and self.checkBox_2.isChecked()):
            k=""
            a=int(self.lineEdit_2.text())
            print('A')
            curr1.execute('select * from stock where item = ? and CP = ?',(self.lineEdit.text(),a))
            rows=curr1.fetchall()
            conn1.commit()
            print(rows[0])
            for row in rows:
                k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"

            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k

            self.textEdit.setText(k)           

        elif(self.checkBox.isChecked() and self.checkBox_3.isChecked()):
            k=""
            
            b=int(self.lineEdit_3.text())
            curr1.execute('select * from stock where item = ? and SP= ?',(self.lineEdit.text(),b))
            rows=curr1.fetchall()
            conn1.commit()

            for row in rows:
                 k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"
            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k
            self.textEdit.setText(k)           
        elif(self.checkBox_3.isChecked() and self.checkBox_2.isChecked()):
            k=""
            a=int(self.lineEdit_2.text())
            b=int(self.lineEdit_3.text())
            curr1.execute('select * from stock where CP=? and SP=?',(a,b))
            rows=curr1.fetchall()
            conn1.commit()
            
            for row in rows:
                k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"
            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k

            self.textEdit.setText(k)           

        elif (self.checkBox.isChecked()):
            k=""
            curr1.execute('select * from stock where item = ?',(self.lineEdit.text(),))
            rows=curr1.fetchall()
            conn1.commit()

            for row in rows:
                   k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"
            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k
            self.textEdit.setText(k)
        elif (self.checkBox_2.isChecked()):
            k=""
            a=int(self.lineEdit_2.text())
            curr1.execute('select * from stock where CP = ?',(a,))
            rows=curr1.fetchall()
            conn1.commit()

            for row in rows:
                   k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"
            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k
            self.textEdit.setText(k)
        elif (self.checkBox_3.isChecked()):
            k=""
            b=int(self.lineEdit_3.text())
            curr1.execute('select * from stock where SP = ?',(b,))
            rows=curr1.fetchall()
            conn1.commit()

            for row in rows:
                   k+="\nName:"+row[0]+"\nCp:"+str(row[1])+"\nSp:"+str(row[5])+"\nQuantity:"+str(row[2])+"\nMFG:"+row[3]+"\nExpiry:"+row[4]+"\n"
            if k=="":
                k="No product match the search criteria. Please try again!!"
            else:
                k="Product details: "+k 

            self.textEdit.setText(k)

        else:
            k="please select a check box"
            self.textEdit.setText(k)

    def search2(self):
        if(self.checkBox_4.isChecked() and self.checkBox_5.isChecked() and self.checkBox_6.isChecked()):
            k=""
            a=self.lineEdit_4.text()
            b=self.lineEdit_5.text()
            c=self.lineEdit_6.text()
            print(a)
            print(b)
            curr3.execute('select * from customer join customer_bought on customer.ID=customer_bought.Id where customer.name= ? and customer_bought.date=? and customer.id=?',(a,b,c))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))
            if len(rows)>0:
                    row=rows[0]
                    k="Name:"+row[1]+"\nAddress:"+row[2]+"\nPhone:"+row[3]+"\nItems bought:"
                    for z in rows:
                        k+="\n "+z[5]+" X "+str(z[6])
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                    k="Customer details\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)
        elif(self.checkBox_5.isChecked() and self.checkBox_6.isChecked()):
            k=""
            b=self.lineEdit_5.text()
            c=self.lineEdit_6.text()
            print(b)
            
            curr3.execute('select * from customer join customer_bought on customer.Id=customer_bought.Id where customer_bought.date= ? and customer.ID=?',(b,c))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))
            if len(rows)>0:
                    row=rows[0]
                    print(rows[0][0])
                    k="Name: "+row[1]+"\nAddress: "+row[2]+"\nPhone: "+row[3]+"\nItems bought:"+"\n  "+row[5]+" X "+str(row[6])
                    for z in range(1,len(rows)):
                        print(z)
                        if rows[z][1]==rows[z-1][1]:
                            k+="\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                            print('a')
                        else:
                            k+="\nDate of store visit:"+"\n"+rows[z-1][7]
                            k+="\n\nName: "+rows[z][1]+"\nAddress: "+rows[z][2]+"\nPhone: "+rows[z][3]+"\nItems bought:"+"\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                        
                    k="Customer details\n\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)
        elif(self.checkBox_4.isChecked() and self.checkBox_5.isChecked()):
            k=""
            b=self.lineEdit_5.text()
            a=self.lineEdit_4.text()
            print(b)
            
            curr3.execute('select * from customer join customer_bought on customer.Id=customer_bought.Id where customer_bought.date= ? and customer.name=?',(b,a))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))
            if len(rows)>0:
                    row=rows[0]
                    print(rows[0][0])
                    k="Name: "+row[1]+"\nAddress: "+row[2]+"\nPhone: "+row[3]+"\nItems bought:"+"\n  "+row[5]+" X "+str(row[6])
                    for z in range(1,len(rows)):
                        print(z)
                        if rows[z][1]==rows[z-1][1]:
                            k+="\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                            print('a')
                        else:
                            k+="\nDate of store visit:"+"\n"+rows[z-1][7]
                            k+="\n\nName: "+rows[z][1]+"\nAddress: "+rows[z][2]+"\nPhone: "+rows[z][3]+"\nItems bought:"+"\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                        
                    k="Customer details\n\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)
        elif(self.checkBox_4.isChecked() and self.checkBox_6.isChecked()):
            k=""
            a=self.lineEdit_4.text()
            c=self.lineEdit_6.text()
            
            
            curr3.execute('select * from customer join customer_bought on customer.Id=customer_bought.Id where customer.name= ? and customer.ID=?',(a,c))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))
            if len(rows)>0:
                    row=rows[0]
                    print(rows[0][0])
                    k="Name: "+row[1]+"\nAddress: "+row[2]+"\nPhone: "+row[3]+"\nItems bought:"+"\n  "+row[5]+" X "+str(row[6])
                    for z in range(1,len(rows)):
                        print(z)
                        if rows[z][1]==rows[z-1][1]:
                            k+="\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                            print('a')
                        else:
                            k+="\nDate of store visit:"+"\n"+rows[z-1][7]
                            k+="\n\nName: "+rows[z][1]+"\nAddress: "+rows[z][2]+"\nPhone: "+rows[z][3]+"\nItems bought:"+"\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                        
                    k="Customer details\n\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)




        elif(self.checkBox_4.isChecked()):
            k=""
            a=self.lineEdit_4.text()
            
            print(a)
            
            curr3.execute('select * from customer join customer_bought on customer.Id=customer_bought.Id where customer.name= ?',(a,))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))

            if len(rows)>0:
                    row=rows[0]
                    print(rows[0][0])
                    k="Name: "+row[1]+"\nAddress: "+row[2]+"\nPhone: "+row[3]+"\nItems bought:"+"\n  "+row[5]+" X "+str(row[6])
                    for z in range(1,len(rows)):
                        print(z)
                        if rows[z][7]==rows[z-1][7]:
                            k+="\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                            print('a')
                        else:
                            k+="\nDate of store visit:"+"\n"+rows[z-1][7]
                            k+="\nItems bought:"+"\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                    k="Customer details\n\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)
        elif(self.checkBox_5.isChecked()):
            k=""
            b=self.lineEdit_5.text()
            
            print(b)
            
            curr3.execute('select * from customer join customer_bought on customer.Id=customer_bought.Id where customer_bought.date= ?',(b,))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))
            if len(rows)>0:
                    row=rows[0]
                    print(rows[0][0])
                    k="Name: "+row[1]+"\nAddress: "+row[2]+"\nPhone: "+row[3]+"\nItems bought:"+"\n  "+row[5]+" X "+str(row[6])
                    for z in range(1,len(rows)):
                        print(z)
                        if rows[z][1]==rows[z-1][1]:
                            k+="\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                            print('a')
                        else:
                            k+="\nDate of store visit:"+"\n"+rows[z-1][7]
                            k+="\n\nName: "+rows[z][1]+"\nAddress: "+rows[z][2]+"\nPhone: "+rows[z][3]+"\nItems bought:"+"\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                        
                    k="Customer details\n\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)
        elif(self.checkBox_6.isChecked()):
            k=""
            b=self.lineEdit_6.text()
            
            print(b)
            
            curr3.execute('select * from customer join customer_bought on customer.Id=customer_bought.Id where customer.ID= ?',(b,))
            rows=curr3.fetchall()
            conn3.commit()
            print(len(rows))
            if len(rows)>0:
                    row=rows[0]
                    print(rows[0][0])
                    k="Name: "+row[1]+"\nAddress: "+row[2]+"\nPhone: "+row[3]+"\nItems bought:"+"\n  "+row[5]+" X "+str(row[6])
                    for z in range(1,len(rows)):
                        print(z)
                        if rows[z][1]==rows[z-1][1]:
                            k+="\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                            print('a')
                        else:
                            k+="\nDate of store visit:"+"\n"+rows[z-1][7]
                            k+="\n\nName: "+rows[z][1]+"\nAddress: "+rows[z][2]+"\nPhone: "+rows[z][3]+"\nItems bought:"+"\n  "+rows[z][5]+" X "+str(rows[z][6])
                            print(k)
                    k+="\nDate of store visit:"+rows[len(rows)-1][7]
                    
                        
                    k="Customer details\n\n"+k
                    print(k)
                    self.textEdit_2.setText(k)
            else:
                k="No such customer found"
                self.textEdit_2.setText(k)
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setup5(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
