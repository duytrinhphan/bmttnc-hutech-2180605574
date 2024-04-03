def chia_het_cho_5(so_nhi_phan):
    # Convert binary number to decimal
    so_thap_phan = int(so_nhi_phan, 2)
    # Check if the decimal number is divisible by 5
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# Get binary numbers from user input
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
# Split the string into a list of binary numbers
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
# Filter the list to keep only the binary numbers that are divisible by 5
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

# Print the result
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là: " + ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")