import sys
from PyQt6.QtWidgets import QApplication, QWidget
from main_layout import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

# chuong trinh chinh 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
