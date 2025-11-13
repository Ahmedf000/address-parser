import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from core.cleanup_pipeline import AddressCleaner

def main():
    app_run = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app_run.exec_()


if __name__ == '__main__':
    cleaner = AddressCleaner()
    Clean_list = [
        cleaner.trim_whitespace,
        cleaner.separate_address,
        cleaner.trim_letters_numbers
    ]

    raw = input("Enter your address: ")
    text = raw

    for func in Clean_list:
        text = func(text)  # update text step by step

    final = text
    print(final)