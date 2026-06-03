import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
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

        # xu ly khi nhan nut search 
        self.btnSearch.clicked.connect(self.xu_ly_tim_kiem)



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

    # Ham xu ly tim kiem 
    def xu_ly_tim_kiem(self):
        # buoc 1: lay du lieu tu giao dien 
        ma_sp = self.txtProductID.text().strip()
        ten_sp = self.txtProductName.text().strip()
        gia = self.txtPrice.text().strip()
        loai = self.cbKindOf.currentText().strip()
        xuat_xu = self.cbOrigin.currentText().strip()
        ghi_chu = self.txtNote.text().strip()

        # buoc 2: Phan luong tim kiem 
        if ma_sp != "" and ten_sp == "": # Nhap ProductID va khong nhap ProductName 
            self.tiem_kiem_theo_ma(ma_sp)
        elif ma_sp == "" and ten_sp != "": # Khong nhap ProductID va chi nhap ProductName
            pass
        elif ma_sp != "" and ten_sp != "": # Nhap ProductID va ProductName (ưu tiên tìm kiếm theo mã sản phẩm
            pass
        else:
            self.hien_thi_thong_bao("Thông báo", "Bạn chưa nhập điều kiện tìm kiếm!")
            self.txtProductID.setFocus()
            return

    # Ham hien thi thong bao 
    def hien_thi_thong_bao(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    # Ham tim kiem theo ma theo ma san pham 
    def tiem_kiem_theo_ma(self, ma_sp):
        # lay du lieu trong csdl 
        data = self.doc_du_lieu()

        # tao danh sach de chua ket qua tim kiem 
        kq = []

        # thuc hien tim kiem 
        for product in data['products']:
            if ma_sp == product['product_id']:
                kq.append(product)

        if len(kq) != 0:
            # hien thi danh sach tim kiem 
            self.tblProduct.clearContents() # xoa noi dung tren bang 
            self.tblProduct.setRowCount(len(kq)) # thiet lap so hang 
            self.tblProduct.setColumnCount(6)  # thiet lap so cot
            
            # hien thi du lieu len bang 
            self.tblProduct.setItem(0, 0, QTableWidgetItem(str(kq[0]['product_id'])))
            self.tblProduct.setItem(0, 1, QTableWidgetItem(str(kq[0]['product_name'])))
            self.tblProduct.setItem(0, 2, QTableWidgetItem(str(kq[0]['price'])))
            self.tblProduct.setItem(0, 3, QTableWidgetItem(str(kq[0]['kind_of'])))
            self.tblProduct.setItem(0, 4, QTableWidgetItem(str(kq[0]['origin'])))
            self.tblProduct.setItem(0, 5, QTableWidgetItem(str(kq[0]['note'])))
            # self.tblProduct.setItem(0, 1, QTableWidgetItem(kq[0]['product_name']))  


# chuong trinh chinh 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
