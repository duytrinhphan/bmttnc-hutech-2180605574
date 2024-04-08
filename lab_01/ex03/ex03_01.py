def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Get user input and convert it to a list of numbers
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers_list = list(map(int, input_list.split(',')))

# Use the function and print the result
tong_chan = tinh_tong_so_chan(numbers_list)
print("Tổng các số chẵn trong List là:", tong_chan)