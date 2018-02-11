#!/usr/bin/env python3

"""
GUI for diabetes prediction.
"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator

import diabetes

class Diabetes(QWidget):

    def __init__(self) -> None :
        super(Diabetes, self).__init__()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.t1 = QLabel("Plasma glucose concentration:")
        self.t2 = QLabel("Diastolic blood pressure:")
        self.t3 = QLabel("Triceps skin fold thickness:")
        self.t4 = QLabel("Serum insulin:")
        self.t5 = QLabel("Body mass index:")
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.clbtn = QPushButton("CLEAR")
        self.submit = QPushButton("SUBMIT")
        self.v_box = QVBoxLayout()
        self.initui()

    def initui(self) -> None:
        """ The gui is created and widgets elements are set here """
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        self.l1.setToolTip("2 hours in an oral glucose tolerance test")
        self.l2.setToolTip("mm Hg")
        self.l3.setToolTip("mm")
        self.l4.setToolTip("mu U/ml")
        self.l5.setToolTip("weight in kg/(height in m)^2")
        self.l1.setFixedSize(40,30)
        self.l2.setFixedSize(40,30)
        self.l3.setFixedSize(40,30)
        self.l4.setFixedSize(40,30)
        self.l5.setFixedSize(40,30)
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)        
        self.v_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)        
        self.v_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)        
        self.v_box.addLayout(self.h3)
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)        
        self.v_box.addLayout(self.h4)
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)        
        self.v_box.addLayout(self.h5)
        self.h6 = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Click to check if patient has diabetes")
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.h6.addWidget(self.submit)
        self.h6.addWidget(self.clbtn)
        self.v_box.addLayout(self.h6)
        self.setLayout(self.v_box)

    def clfn(self):
        """ clear all the text fields via clear button"""
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()

    def test_input(self) -> None:
        """ test for diabetes"""
        my_dict = {"B":float(self.l1.text()), "C":float(self.l2.text()),"D":float(self.l3.text()), "E":float(self.l4.text()), "F": float(self.l5.text())}
        output = diabetes.check_input(my_dict)
        #print(self.output)
        msg = QMessageBox()
        msg.setWindowTitle("Prediction")
        #
        if output==0:
            msg.setText("You do not seem to have diabetes.")
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setText("There is 80% chance that you have diabetes.")
            msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        
       
    def mwindow(self) -> None:
        """ window features are set here and application is loded into display"""
        self.setFixedSize(300, 300)
        self.setWindowTitle("Diabetes Detection")
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Diabetes()
    a_window.mwindow()
    sys.exit(app.exec_())
