from PyQt6.QtWidgets import QWidget, QPushButton
from ui_widget import Ui_widget

import math



class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.setGeometry(200,455,300,400)

        self.button_0.clicked.connect(self.on_button_click)
        self.button_1.clicked.connect(self.on_button_click)
        self.button_2.clicked.connect(self.on_button_click)
        self.button_3.clicked.connect(self.on_button_click)
        self.button_4.clicked.connect(self.on_button_click)
        self.button_5.clicked.connect(self.on_button_click)
        self.button_6.clicked.connect(self.on_button_click)
        self.button_7.clicked.connect(self.on_button_click)
        self.button_8.clicked.connect(self.on_button_click)
        self.button_9.clicked.connect(self.on_button_click)
        self.button_plus.clicked.connect(self.on_button_click)
        self.button_minus.clicked.connect(self.on_button_click)
        self.button_multi.clicked.connect(self.on_button_click)
        self.button_divide.clicked.connect(self.on_button_click)
        self.button_decimal.clicked.connect(self.on_button_click)
        self.button_equals.clicked.connect(self.on_button_click)
        self.button_c.clicked.connect(self.on_button_click)



    def on_button_click(self):
        button = self.sender()
        print(button.text())
        currnet_text = self.main_label.text()

        if currnet_text == "0":
            currnet_text = ""
        
        if button.text() == "=":
            try:
                result = eval(currnet_text)
                self.main_label.setText(str(round(result, 2)))
                self.main_label_2.setText(currnet_text + button.text())
            except ZeroDivisionError:
                self.main_label.setText("Error : Division by zero")
            except Exception as e:
                self.main_label.setText(f"Error : {e}")
                print(f"Error : {e}")
        else:
            self.main_label.setText(currnet_text + button.text())
            self.main_label_2.setText(currnet_text + button.text())
        
        if button.text() == "C":
            self.main_label.setText("")
            self.main_label_2.setText("")
            return
