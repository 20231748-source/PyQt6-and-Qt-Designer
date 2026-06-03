# them modulo
from list_function import * # tất cả của file list

# khai bao ham
def start():
    s = """Chào mừng bạn đến với chương trình của tôi: 
    1. Hiển thị thông tin các sản phẩm trong dự án.
    2. Hiển thị thông tin các sản phẩm theo giá tiền hoặc loại sản phẩm. 
    3. Thêm thông tin của một sản phẩm vào cửa hàng. 
    4. Chỉnh sửa các thông tin của một sản phầm theo mã sản phẩm. 
    5. Xoá một sản phẩm trong cửa hàng theo mã sản phẩm.
    6. Thoát khỏi chương trình.\n 
    Mời bạn nhập vào sự lựa chọn chức năng: """ 
    lua_chon = input(s).strip()
    chuc_nang = int(lua_chon)
    if lua_chon.isnumeric() and chuc_nang > 0 and chuc_nang < 7:
        if chuc_nang == 1:
            hien_thi_danh_sach_san_pham()
            start()
        elif chuc_nang == 2:
            choice = int(input("""
        1. Hiển thị danh sách sản phẩm theo giá tiền.
        2. Hiển thị danh sách sản phẩm theo loại sản phẩm. 
        Mời bạn nhập vào sự lựa chọn: """))
            if choice == 1:
                hien_thi_danh_sach_theo_gia()
                start()
            elif choice == 2:
                hien_thi_danh_sach_theo_loai()
                start()
            else:
                print("Bạn nhập sai chức năng. Mời nhập lại!")
                start()
        elif chuc_nang == 3:
            them_san_pham()
            start()            
        elif chuc_nang == 4:
            chinh_sua_thong_tin_theo_ma()
            start()
        elif chuc_nang == 5:
            xoa_san_pham()
            start()
        elif chuc_nang == 6:
            print("Cảm ơn bạn đã sử dụng chương trình của chúng tôi!.")
    else:
        print("Bạn nhập sai chức năng. Mời nhập lại!")
        start()


# chuong trinh chinh 
if __name__ == '__main__':
    start()