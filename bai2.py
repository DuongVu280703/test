import tkinter as tk

def scan_now():
    status_label.config(text="Đang quét...")

def quick_scan():
    status_label.config(text="Đang quét nhanh...")

def web_protect():
    status_label.config(text="Đang bảo vệ web...")

def isolate():
    status_label.config(text="Đang cách ly...")

def full_scan():
    status_label.config(text="Đang quét toàn bộ...")

def update():
    status_label.config(text="Đang cập nhật...")

def exit_program():
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giao diện quét")

# Cấu hình kích thước cửa sổ và màu nền
root.geometry("800x500")
root.configure(bg="#f0f0f0")

# Tạo khung chính
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Thanh bên (left frame)
left_frame = tk.Frame(main_frame, bg="#faebd7", width=200)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# Nhãn và nút trong thanh bên
status_label = tk.Label(left_frame, text="Không có hoạt động", font=("Arial", 12), bg="#faebd7", padx=10, pady=10)
status_label.pack(pady=20)

status_button = tk.Button(left_frame, text="Trạng thái", width=15)
status_button.pack(pady=5)

update_button = tk.Button(left_frame, text="Cập nhật", width=15, command=update)
update_button.pack(pady=5)

support_button = tk.Button(left_frame, text="Hỗ trợ", width=15)
support_button.pack(pady=5)

exit_button = tk.Button(left_frame, text="Thoát chương trình", width=15, command=exit_program)
exit_button.pack(pady=5)

scan_now_button = tk.Button(left_frame, text="Quét ngay", width=15, command=scan_now)
scan_now_button.pack(pady=20)

# Khu vực chính (right frame)
right_frame = tk.Frame(main_frame, bg="#f0ffff", padx=20, pady=20)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Nhãn tiêu đề và phụ đề
title_label = tk.Label(right_frame, text="Phần mềm quét máy tính", font=("Arial", 20), bg="#f0ffff")
title_label.pack()

subtitle_label = tk.Label(right_frame, text="Phiên bản 1.0.0", font=("Arial", 12), bg="#f0ffff")
subtitle_label.pack()

# Nút cho các chức năng khác
quick_scan_button = tk.Button(right_frame, text="Quét nhanh", width=15, command=quick_scan)
quick_scan_button.pack(pady=10)

web_protect_button = tk.Button(right_frame, text="Bảo vệ web", width=15, command=web_protect)
web_protect_button.pack(pady=10)

isolate_button = tk.Button(right_frame, text="Cách ly", width=15, command=isolate)
isolate_button.pack(pady=10)

full_scan_button = tk.Button(right_frame, text="Quét toàn bộ", width=15, command=full_scan)
full_scan_button.pack(pady=10)

update_button_main = tk.Button(right_frame, text="Cập nhật", width=15, command=update)
update_button_main.pack(pady=10)

# Chạy cửa sổ chính
root.mainloop()
