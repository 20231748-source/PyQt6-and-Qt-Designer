import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from main_layout import Ui_Form
# thu vien json
import json
class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ket noi bien trong file hien tai voi thanh phan giao dien o file giao dien py
        self.txtProductID = self.ui.txtProductID
        self.txtProductName = self.ui.txtProductName
        self.txtPrice = self.ui.txtPrice
        self.cbKindOf = self.ui.cbKindOf
        self.cbOrigin = self.ui.cbOrigin
        self.txtNote = self.ui.txtNote

        # ket noi button
        self.btnAdd = self.ui.btnAdd
        self.btnUpdate = self.ui.btnUpdate
        self.btnDelete = self.ui.btnDelete
        self.btnClear = self.ui.btnClear
        self.btnSearch = self.ui.btnSearch
        self.btnSelect = self.ui.btnSelect

        # ket noi bang
        self.tblProduct = self.ui.tblProduct

        # Ham hien thi du lieu len tren bang tablewidget
        self.hien_thi_thong_tin()

    # Ham doc du lieu trong file json 
    def doc_du_lieu(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        return data

    # Ham hien thi du lieu len tren bang tablewidget
    def hien_thi_thong_tin(self):
        # xoa du lieu tren giao dien 
        self.tblProduct.clearContents()
        self.tblProduct.setRowCount(0)

        # doc du lieu tu file json
        data = self.doc_du_lieu()

        # thiet lap so hang 
        self.tblProduct.setRowCount(len(data['products']))

        # thiet lap so cot
        self.tblProduct.setColumnCount(6)

        # hien thi du lieu len ten tablewidget
        i = 0
        for product in data['products']:
            self.tblProduct.setItem(i, 0, QTableWidgetItem(str(product['product_id'])))
            self.tblProduct.setItem(i, 1, QTableWidgetItem(product['product_name']))
            self.tblProduct.setItem(i, 2, QTableWidgetItem(str(product['price'])))
            self.tblProduct.setItem(i, 3, QTableWidgetItem(product['kind_of']))
            self.tblProduct.setItem(i, 4, QTableWidgetItem(product['origin']))
            self.tblProduct.setItem(i, 5, QTableWidgetItem(product['note']))
            i += 1

# chuong trinh chinh 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
