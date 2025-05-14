import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
import tkinter as tk
from analysis import DataAnalyzer
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
data = pd.read_csv('adult.csv')
analize = DataAnalyzer(data)

info = analize.summary()

def information():
    try:
        text_area.delete('1.0', tk.END) #To clean out when running
        info = analize.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror('Error')


root = tk.Tk()

boton_summary = tk.Button(root, text='Summary', command=information)
boton_summary.pack()

text_area = ScrolledText(root, width=70, height=30)
text_area.pack()


root.mainloop()

