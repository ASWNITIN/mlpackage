import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import subprocess
import os
from tkinter import messagebox

def open_image():
    image_path = filedialog.askopenfilename(title="Select an Image")
    if image_path:
        os.system(f'start {image_path}')

def train_model():
    try:
        subprocess.run(["python", "C:/Nitin/Projects/FDIA-PdM-master/FDIA-PdM-master/src/regression_LSTM.py"], check=True)
        messagebox.showinfo("Training Model", "Training completed.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to run the training script.")

def test_model():
    try:
        subprocess.run(["python", "C:/Nitin/Projects/FDIA-PdM-master/FDIA-PdM-master/src/regression_LSTM_test.py"], check=True)
        messagebox.showinfo("Testing Model", "Testing completed.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to run the testing script.")

root = tk.Tk()
root.title("Regression LSTM Model")

# Create a larger frame with improved styling
style = ttk.Style()
style.configure("TButton", padding=(10, 5))
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

train_button = ttk.Button(frame, text="Train Model", command=train_model)
test_button = ttk.Button(frame, text="Test Model", command=test_model)
display_button = ttk.Button(frame, text="Display Image", command=open_image)

train_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
test_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
display_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

root.mainloop()
