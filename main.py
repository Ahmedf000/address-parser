import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

def main():
    app_run = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app_run.exec_()


if __name__ == '__main__':
    main()