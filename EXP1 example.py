import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def plot_signal():
    try:
        num_points = int(num_points_entry.get())
        start_point = int(start_point_entry.get())
        values = [float(x) for x in values_entry.get().split()]
        
        n1 = np.arange(start_point, start_point + num_points)
        
        plt.figure()
        plt.stem(n1, values, linefmt='b-', markerfmt='ro', basefmt=' ')
        plt.title("Custom Discrete Signal")
        plt.xlabel("Data points")
        plt.ylabel("Values")
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please check your input values.")

# Create main window
root = tk.Tk()
root.title("Custom Discrete Time Signal Creator")

# Create input fields
tk.Label(root, text="Number of Data Points:").grid(row=0, column=0)
num_points_entry = tk.Entry(root)
num_points_entry.grid(row=0, column=1)

tk.Label(root, text="Starting Point of Data Points on Axis:").grid(row=1, column=0)
start_point_entry = tk.Entry(root)
start_point_entry.grid(row=1, column=1)

tk.Label(root, text="Values (separated by space):").grid(row=2, column=0)
values_entry = tk.Entry(root)
values_entry.grid(row=2, column=1)

# Create button to plot signal
plot_button = tk.Button(root, text="Plot Signal", command=plot_signal)
plot_button.grid(row=3, columnspan=2)

root.mainloop()
