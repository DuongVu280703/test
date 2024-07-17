import tkinter as tk
from tkinter import messagebox


def submit_data():
    # Lấy dữ liệu từ các trường nhập liệu
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    job_title = job_title_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()

    # Lấy dữ liệu từ các hộp kiểm
    registration_status = registration_status_var.get()
    completed_courses = completed_courses_spinbox.get()
    semester = semester_spinbox.get()

    # Kiểm tra trạng thái chấp nhận điều khoản và điều kiện
    if accept_terms_checkbox_var.get() == 1:
        terms_accepted = "Đã chấp nhận"
    else:
        terms_accepted = "Chưa chấp nhận"

    # In thông tin ra bảng điều khiển
    message = f"""Thông tin người dùng:
    Tên: {first_name} {last_name}
    Chức danh: {job_title}
    Tuổi: {age}
    Quốc tịch: {nationality}

    Trạng thái đăng ký: {registration_status}
    Số khóa học đã hoàn thành: {completed_courses}
    Học kỳ: {semester}

    Điều khoản và điều kiện: {terms_accepted}
    """
    messagebox.showinfo("Thông tin người dùng", message)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đăng ký thông tin người dùng")
root.geometry("500x400")

# Khung thông tin người dùng
user_info_frame = tk.LabelFrame(root, text="Thông tin người dùng")
user_info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Tên
tk.Label(user_info_frame, text="Tên:").grid(row=0, column=0, sticky="w")
first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

# Họ
tk.Label(user_info_frame, text="Họ:").grid(row=1, column=0, sticky="w")
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Chức danh
tk.Label(user_info_frame, text="Chức danh:").grid(row=2, column=0, sticky="w")
job_title_entry = tk.Entry(user_info_frame)
job_title_entry.grid(row=2, column=1, padx=10, pady=5)

# Tuổi
tk.Label(user_info_frame, text="Tuổi:").grid(row=3, column=0, sticky="w")
age_entry = tk.Entry(user_info_frame)
age_entry.grid(row=3, column=1, padx=10, pady=5)

# Quốc tịch
tk.Label(user_info_frame, text="Quốc tịch:").grid(row=4, column=0, sticky="w")
nationality_entry = tk.Entry(user_info_frame)
nationality_entry.grid(row=4, column=1, padx=10, pady=5)

# Khung đăng ký
registration_frame = tk.LabelFrame(root, text="Đăng ký")
registration_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Trạng thái đăng ký
registration_status_var = tk.IntVar()
registration_status_var.set(0)
registration_status_check = tk.Checkbutton(registration_frame, text="Đã đăng ký", variable=registration_status_var)
registration_status_check.grid(row=0, column=0, padx=10, pady=5)

# Số khóa học đã hoàn thành
tk.Label(registration_frame, text="Số khóa học đã hoàn thành:").grid(row=1, column=0, sticky="w")
completed_courses_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)
completed_courses_spinbox.grid(row=1, column=1, padx=10, pady=5)

# Học kỳ
tk.Label(registration_frame, text="Học kỳ:").grid(row=2, column=0, sticky="w")
semester_spinbox = tk.Spinbox(registration_frame, from_=1, to=8)
semester_spinbox.grid(row=2, column=1, padx=10, pady=5)

# Khung Điều khoản và Điều kiện
terms_conditions_frame = tk.LabelFrame(root, text="Điều khoản và Điều kiện")
terms_conditions_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Điều khoản và Điều kiện
accept_terms_checkbox_var = tk.IntVar()
accept_terms_checkbox = tk.Checkbutton(terms_conditions_frame, text="Tôi đồng ý với các điều khoản và điều kiện",
                                       variable=accept_terms_checkbox_var)
accept_terms_checkbox.grid(row=0, column=0, padx=10, pady=5)

# Nút Gửi
submit_button = tk.Button(root, text="Gửi", width=10, command=submit_data)
submit_button.pack(pady=10)

# Chạy cửa sổ chính
root.mainloop()
