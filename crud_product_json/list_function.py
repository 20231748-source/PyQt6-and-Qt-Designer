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