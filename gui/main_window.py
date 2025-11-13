"""
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
        self.button = QPushButton("Clean Address")
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
        self.input.setObjectName("input_editor")
        self.output.setObjectName("output_editor")


        self.setStyleSheet("""
        #input_editor {
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            border-radius: 6px;
            padding: 8px;  
            font-family: Consolas, monospace;
            font-size: 30px;
            color: #333;      
        }
        #output_editor {
            background-color: #f0f0f0;
            border: 1px solid #bbb;
            border-radius: 6px;
            padding: 8px;
            font-family: Consolas, monospace;
            font-size: 30px;
            color: #222;
        }
        #button_editor { 
            color: black;
            border: 1px solid #555;
            border-radius: 6px;
            padding: 10px 26px;
            font-weight: bold;
            font-size: 16px;
            letter-spacing: 0.5px;
        }
        #button_editor:hover {
            background-color: white;
            border: 1px solid #777;
            color: black;
            cursor: pointer;
        }
        """)

        central_widget.setLayout(vbox)

        self.button.clicked.connect(self.clean_up)

    def clean_up(self):
        text = self.input.toPlainText()
        clean = text.strip()
        self.output.setText(clean)


