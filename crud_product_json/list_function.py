# them thu vien 
import json

# Ham doc du lieu tu tep 
def doc_data_tu_tep():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)
    

# Doc thong tin tu tep
data = doc_data_tu_tep() # bien toan cuc
print(data)

# Ham hien thi thong tin chi tiet cac san pham trong cua hang 
def hien_thi_danh_sach_san_pham():
    print("Danh sách các sản phẩm trong cửa hàng là:")
    i = 1
    for pro in data["products"]:
        print("Sản phẩm thứ: " + str(i) + " là: ")
        print("\t")
        print("\tMã sản phâm: " + str(pro["pro_id"]))
        print("\tTên sản phâm: " + str(pro["pro_name"]))
        print("\tGiá sản phâm: " + str(pro["pro_price"]))
        print("\tSố lượng sản phâm: " + str(pro["pro_amount"]))
        print("\tLoại sản phâm: " + str(pro["pro_kind_of"]))
        i += 1
        

# Ham hien thi danh sach san pham theo gia         
def hien_thi_danh_sach_theo_gia():
    gia = int(input("Mời bạn nhập vào giá sản phẩm cao nhất: "))
    i = 1
    for pro in data["products"]:
        if pro["pro_price"] < gia:
            print("Sản phẩm thứ: " + str(i) + " là: ")
            print("\t")
            print("\tMã sản phâm: " + str(pro["pro_id"]))
            print("\tTên sản phâm: " + str(pro["pro_name"]))
            print("\tGiá sản phâm: " + str(pro["pro_price"]))
            print("\tSố lượng sản phâm: " + str(pro["pro_amount"]))
            print("\tLoại sản phâm: " + str(pro["pro_kind_of"]))
            i += 1
        
# Ham hien thi danh sach san pham theo loai san pham 
def hien_thi_danh_sach_theo_loai():
    loai = input("Mời bạn nhập vào giá sản phẩm cao nhất: ")
    i = 1
    for pro in data["products"]:
        if pro["pro_kind_of"] == loai:
            print("Sản phẩm thứ: " + str(i) + " là: ")
            print("\t")
            print("\tMã sản phâm: " + str(pro["pro_id"]))
            print("\tTên sản phâm: " + str(pro["pro_name"]))
            print("\tGiá sản phâm: " + str(pro["pro_price"]))
            print("\tSố lượng sản phâm: " + str(pro["pro_amount"]))
            print("\tLoại sản phâm: " + str(pro["pro_kind_of"]))
            i += 1

# Ham them mot san pham 
def them_san_pham():
    _id = int(input("Mời bạn nhập vào mã sản phẩm: "))
    _ten = input("Mời bạn nhập vào tên sản phẩm: ")
    _gia = int(input("Mời bạn nhập vào giá sản phẩm: "))
    _so_luong = int(input("Mời bạn nhập vào số lượng sản phẩm: "))
    _loai = input("Mời bạn nhập vào loại sản phẩm: ")
    
    # Cau truc cua 1 san pham 
    product = {
        "pro_id": _id,
        "pro_name": _ten,
        "pro_price": _gia,
        "pro_amount": _so_luong,
        "pro_kind_of": _loai
    }

    # them san pham moi vao danh sach 
    data["products"].append(product)
    print("Thêm sản phẩm thành công!")
    print(data)
    # ghi du lieu vao tep
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Ham chinh sua thong tin 
def chinh_sua_thong_tin_theo_ma():
    _id = int(input("Mời bạn nhập vào mã sản phẩm cần chỉnh sửa: "))
    kt = 0 
    for pro in data["products"]:
        if pro["pro_id"] == _id:
            kt = 1
            _ten = input("Mời bạn nhập vào tên sản phẩm muốn sửa đổi: ")
            _gia = int(input("Mời bạn nhập vào giá sản phẩm muốn sửa đổi: "))
            _so_luong = int(input("Mời bạn nhập vào số lượng sản phẩm muốn sửa đổi: "))
            _loai = input("Mời bạn nhập vào loại sản phẩm muốn sửa đổi: ")

            pro["pro_name"] = _ten
            pro["pro_price"] = _gia
            pro["pro_amount"] = _so_luong
            pro["pro_kind_of"] = _loai
            
        if kt == 0:
            print("Không có sản phẩm như bạn vừa nhập!")
        else:
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            print("Chỉnh sửa sản phẩm thành công!")
            print(data)

# Ham xoa san pham 
def xoa_san_pham():
    _id = int(input("Mời bạn nhập vào mã sản phẩm cần xóa: "))
    kt = 0
    for pro in data["products"]:
        if pro["pro_id"] == _id:
            kt = 1
            data["products"].pop(data["products"].index(pro))
            break
    if kt == 0:
        print("Không có sản phẩm như bạn vừa nhập!")
    else:
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Xóa sản phẩm thành công!")
        print(data)