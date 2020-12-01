from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title("YT Downloader")
root.geometry("350x400")
root.columnconfigure(0, weight=1)

ytdLabel = Label(root, text= "Enter the URL of the video", font= ("jost", 15))
ytdLabel.grid()

root.mainloop()