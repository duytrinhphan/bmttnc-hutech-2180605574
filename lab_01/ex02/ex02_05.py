# Nhập số giờ làm mỗi tuần
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))

# Nhập thù lao trên mỗi giờ làm tiêu chuẩn
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

# Số giờ làm chuẩn mỗi tuần
gio_tieu_chuan = 44

# Số giờ làm vượt chuẩn
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tính tổng thu nhập
thuc_linh = luong_gio * gio_tieu_chuan + gio_vuot_chuan * luong_gio * 1.5

# Print the resulting income
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")