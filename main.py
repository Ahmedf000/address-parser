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

    raw = input("Enter your address: ")
    cleaned = cleaner.clean(raw)

    print("\n" + "=" * 50)
    print("Original address:")
    print(raw)
    print("\n" + "=" * 50)
    print("Cleaned address:")
    print(cleaned)
    print("=" * 50)