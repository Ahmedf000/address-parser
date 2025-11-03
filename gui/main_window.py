"""
MainWindow Module

All the styling and GUI adjusting worked within this file

--------------------
Author: Ahmed Farid
Date: 11/03/2025
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Address Parser")
        self.setGeometry(700, 300, 800, 500)
        self.input = QTextEdit()
        self.button = QPushButton("Clean up")
        self.output = QTextEdit()
        self.build_ui()


    def build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()

        vbox.addWidget(self.input)
        vbox.addWidget(self.button)
        vbox.addWidget(self.output)

        self.button.setObjectName("button_editor")

        self.button.setStyleSheet("""
        #button_editor { 
            background-color: black;
            color: white;
            border-radius: 5px;
            top-padding: 20px;
            button-padding: 20px;
        }
        #button_editor::hover {
        background-color: white;
        color: black;
        }
        
        """)

        central_widget.setLayout(vbox)


