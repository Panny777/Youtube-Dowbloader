from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
 
root = tk.Tk()
root.title("Yotube Download")
root.geometry("380x90")
root.resizable(False, False)

link_var = tk.StringVar()

def submit():
    link = link_var.get()
    #ask for the link from user
    yt = YouTube(link)

    #Showing details
    name_label = tk.Label(root, text = 'Title:', font=('calibre',10, 'bold'))
    name_label.place(x=5, y=40)

    name_label2 = tk.Label(root, text = yt.title, font=('calibre',10))
    name_label2.place(x=40, y=40)

    time.sleep(2)
    
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)

    #Starting download
    print("Downloading...")

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()
    
    ys.download()
    messagebox.showinfo("", "Download completed!!")
    link_entry.delete(0, 'end')

name_label = tk.Label(root, text = 'Link', font=('calibre',10, 'bold'))
name_label.place(x=5, y=0)

link_entry = tk.Entry(root, textvariable = link_var, font=('calibre',10,'normal'), width= 50)
link_entry.place(x=5, y=20)

print(link_var.get())

sub_btn=tk.Button(root,text = 'Download', command = submit)
sub_btn.pack(side = BOTTOM )

root.mainloop()

