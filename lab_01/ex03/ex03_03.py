def tao_tuple_tu_list(lst):
    return tuple(lst)
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers_list = list(map(int, input_list.split(',')))

# Tạo tuple và in kết quả
my_tuple = tuple(numbers_list)
print("List: ", numbers_list)
print("Tuple từ List:", my_tuple)