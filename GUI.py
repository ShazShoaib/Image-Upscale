import tkinter as tk
from tkinter import filedialog
import ntpath
from functools import partial
from Upscale import *

file_path = ""
def temp(a,b):
    if file_path == '':
        return
    iter = str(text_box.get("1.0",'end-1c'))
    if  iter == '':
        iter = 1
    else:
        iter = (int(iter))
    interpolateGUI(file_path,iter)

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select attachment")
    file_path_label.configure(text=ntpath.basename(file_path))
    print("Selected File:", file_path)

root = tk.Tk()
root.title("Image Upscaler")
root.geometry("400x125")

file_path_label = tk.Label(root, text="No file selected", anchor="w")
factor_label = tk.Label(root, text="Select Upscale Iterations :", anchor="w")
factor_label.place(x=210, y=15, height=40, width=170)

file_img = tk.PhotoImage(file='Icons/file.png')
file_button = tk.Button(root, command=select_file, image=file_img)
file_button.place(x=15, y=15, height=40, width=40)
file_path_label.place(x=65,y=15,height=40,width=160)

font_tuple = ("Calibri", 11, "")
text_box = tk.Text(root)
text_box.configure(font=font_tuple)
text_box.place(x=350, y=25, height=20, width=20)

upscale_command = partial(temp,file_path,text_box.get("1.0",'end-1c'))
upscale_button = tk.Button(root, text="Upscale", command= upscale_command)
upscale_button.place(x=150, y=65, height=40, width=100)

root.mainloop()