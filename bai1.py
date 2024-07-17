import tkinter as tk

# Hàm để bắt đầu FPS
def start_fps():
    global fps_running
    fps_running = True
    status_label.config(text="Đang ghi...")
    start_button.config(state=tk.DISABLED)
    pause_button.config(state=tk.NORMAL)
    end_button.config(state=tk.DISABLED)
    print("Bắt đầu ghi FPS")

# Hàm để tạm dừng FPS
def pause_fps():
    global fps_running
    fps_running = False
    status_label.config(text="Tạm dừng ghi")
    start_button.config(state=tk.NORMAL)
    pause_button.config(state=tk.DISABLED)
    end_button.config(state=tk.NORMAL)
    print("Tạm dừng ghi FPS")

# Hàm để kết thúc chương trình
def end_program():
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ghi FPS")

# Cấu hình kích thước cửa sổ và màu nền
root.geometry("600x300")
root.configure(bg="#faebd7")

# Nhãn tiêu đề
title_label = tk.Label(root, text="Ghi FPS", font=("Arial", 24), bg="#faebd7")
title_label.pack(pady=20)

# Đầu vào FPS
fps_entry = tk.Entry(root, width=10, font=("Arial", 14))
fps_entry.pack()

# Hàng nút
button_frame = tk.Frame(root, bg="#faebd7")
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Bắt đầu", width=10, command=start_fps)
start_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(button_frame, text="Tạm dừng", width=10, command=pause_fps, state=tk.DISABLED)
pause_button.grid(row=0, column=1, padx=10)

end_button = tk.Button(button_frame, text="Kết thúc", width=10, command=end_program)
end_button.grid(row=0, column=2, padx=10)

# Nhãn trạng thái
status_label = tk.Label(root, text="Không ghi", font=("Arial", 18), bg="#faebd7")
status_label.pack(pady=20)

# Biến để lưu trạng thái chạy FPS
fps_running = False

# Chạy cửa sổ chính
root.mainloop()
