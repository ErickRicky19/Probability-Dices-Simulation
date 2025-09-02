import customtkinter as ctk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
min_value = 1
max_value = 6
result1 = []
result2 = []

def update_min_max():
    global min_value, max_value
    try:
        new_min = int(entry_min.get())
        new_max = int(entry_max.get())
        if new_min > new_max:
            messagebox.showerror("Error", "minimun value cannot be greater than maximum.")
            return
        min_value = new_min
        max_value = new_max
        messagebox.showinfo("Updated", f"New values published:\nMinimun: {min_value}\nMaximun: {max_value}")
    except ValueError:
        messagebox.showerror("Error", "Please, insert a valid number.")

def show_report():
    report_window = tk.Toplevel()
    report_window.title("Probability Report")
    report_window.geometry("1000x800")

    fig1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = fig1.add_subplot(111)
    sns.histplot(result1, bins=20, kde=True, color='steelblue', ax=ax1)
    ax1.set_title('Diagram of probability from dice 1')
    ax1.set_xlabel('Cant of combinations')
    ax1.set_ylabel('Frecuency')

    canvas1 = FigureCanvasTkAgg(fig1, master=report_window)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    fig2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = fig2.add_subplot(111)
    sns.histplot(result2, bins=20, kde=True, color='darkorange', ax=ax2)
    ax2.set_title('Diagram of probability from dice 2')
    ax2.set_xlabel('Cant of combinations')
    ax2.set_ylabel('Frecuency')

    canvas2 = FigureCanvasTkAgg(fig2, master=report_window)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
def launch_dices():
    canvas.delete("all")
    try:
        value1 = random.randint(min_value, max_value)
        value2 = random.randint(min_value, max_value)
        result1.append(value1)
        result2.append(value2)
        draw_dice(canvas, 85, 200, 500, value1)
        draw_dice(canvas, 800, 200, 500, value2)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def draw_dice(canvas, x, y, size, value):
    canvas.create_rectangle(x, y, x + size, y + size, fill="white", outline="black", width=3)

    if 1 <= value <= 6:
        pip_radius = size // 10
        offset = size // 4

        positions = {
            1: [(x + size // 2, y + size // 2)],
            2: [(x + offset, y + offset), (x + size - offset, y + size - offset)],
            3: [(x + offset, y + offset), (x + size // 2, y + size // 2), (x + size - offset, y + size - offset)],
            4: [(x + offset, y + offset), (x + size - offset, y + offset),
                (x + offset, y + size - offset), (x + size - offset, y + size - offset)],
            5: [(x + offset, y + offset), (x + size - offset, y + offset),
                (x + size // 2, y + size // 2),
                (x + offset, y + size - offset), (x + size - offset, y + size - offset)],
            6: [(x + offset, y + offset), (x + size - offset, y + offset),
                (x + offset, y + size // 2), (x + size - offset, y + size // 2),
                (x + offset, y + size - offset), (x + size - offset, y + size - offset)],
        }

        for px, py in positions[value]:
            canvas.create_oval(px - pip_radius, py - pip_radius, px + pip_radius, py + pip_radius, fill="black")
    else:
        canvas.create_text(x + size // 2, y + size // 2, text=str(value), font=("Arial", 50, "bold"), fill="black")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Binary Tree - Binary Tree Test")
root.geometry("1500x500")

frame_controls = ctk.CTkFrame(root)
frame_controls.pack(side=ctk.LEFT, padx=10, pady=10)

frame_title = ctk.CTkFrame(frame_controls)
frame_title.pack(pady=20)
label_value = ctk.CTkLabel(frame_title, text="Binary Tree Test", font=("Arial", 50, "bold"), text_color="#FFF")
label_value.pack(side=ctk.TOP, padx=5, pady=10)

frame_write = ctk.CTkFrame(frame_controls)
frame_write.pack(pady=5)

label_min = ctk.CTkLabel(frame_write, text="Minimun Value:", font=("Arial", 16, "bold"), text_color="#FFF")
label_min.pack(side=ctk.LEFT, padx=5, pady=10)

entry_min = ctk.CTkEntry(frame_write, font=("Arial", 14), width=380)
entry_min.insert(0, str(min_value))
entry_min.pack(side=ctk.LEFT, padx=5, pady=10)


frame_max = ctk.CTkFrame(frame_controls)
frame_max.pack(pady=5)

label_max = ctk.CTkLabel(frame_max, text="Maximun Value:", font=("Arial", 16, "bold"), text_color="#FFF")
label_max.pack(side=ctk.LEFT, padx=5, pady=10)

entry_max = ctk.CTkEntry(frame_max, font=("Arial", 14), width=380, )
entry_max.insert(0, str(max_value))
entry_max.pack(side=ctk.LEFT, padx=5, pady=10)

frame_range = ctk.CTkFrame(frame_controls)
frame_range.pack(pady=10)


button_update_range = ctk.CTkButton(frame_range, text="🔄 Update Values", command=update_min_max)
button_update_range.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
button_roll_dice = ctk.CTkButton(frame_range, text="🎲 Launce Dices", command=launch_dices)
button_roll_dice.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
button_show_reports = ctk.CTkButton(frame_range, text="Show Reports", command=show_report)
button_show_reports.grid(row=4, column=0, columnspan=2, pady=10, padx=10)


frame_canvas = ctk.CTkFrame(root, bg_color='white')
frame_canvas.pack(side=ctk.RIGHT, pady=1, padx=1)

canvas = ctk.CTkCanvas(frame_canvas, width=1900, height=900, bg='#2D2D2D')
canvas.pack(pady=1, padx=1)

# Ejecutar aplicación
root.mainloop()
