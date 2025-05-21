import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
import tkinter as tk
from analysis import DataAnalyzer
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, simpledialog, filedialog
from PIL import ImageTk
data = pd.read_csv('adult.csv')
analize = DataAnalyzer(data, 'adult.csv')

info = analize.summary()

def information():
    try:
        text_area.delete('1.0', tk.END) #To clean out when running
        info = analize.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror('Error')

def show_images(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    image_label.configure(image=image_tk)
    image_label.image = image_tk

def show_correlation():
    img = analize.correlation_matrix()
    show_images(img)

def show_categorical():
    cols = analize.df.select_dtypes(include='object').columns.tolist()
    if not cols:
        messagebox.showwarning("Attention, the df doesn't have categorical columns")
    else:
        sel = simpledialog.askstring('Column', f'Choose a:\n {cols}')
        if sel in cols:
            img = analize.categorical_analisis_col(sel)
            show_images(img)

def add_value():
    try:
        col = simpledialog.askstring('Column', 'Enter column name:')
        val = simpledialog.askstring('Value', f'Enter value to add in column "{col}":')
        if col and val:
            analize.new_value(col, val)
            messagebox.showinfo('Success', f'Value "{val}" added to column "{col}".')
        else:
            messagebox.showwarning('Input needed', 'Both column and value are required.')
    except Exception as e:
        messagebox.showerror('Error', str(e))


root = tk.Tk()
root.title('Data Analysis')

boton_summary = tk.Button(root, text='Summary', command=information)
boton_summary.grid(row=0, column=0)

numeric_button = tk.Button(root, text='Numeric', command=show_correlation)
numeric_button.grid(row=0, column=1)

categorical_button = tk.Button(root, text='Categorical', command=show_categorical)
categorical_button.grid(row=0, column=2)

text_area = ScrolledText(root, width=70, height=30)
text_area.grid(row=1, column=1)

add_button = tk.Button(root, text='Add Value', command=add_value)
add_button.grid(row=0, column=3)


content_frame = tk.Frame(root)
content_frame.grid(row=1, column=2)
image_label = tk.Label(content_frame)
image_label.grid(row=0, column=0)
root.mainloop()



