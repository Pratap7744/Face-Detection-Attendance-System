from tkinter import *
main_window=Tk()
main_window.title("Image Fusion")
main_window.geometry("590x500")

def start():
    print("Hello")

l = Label(main_window, text = " Image Fusion ")
l.config(font =("Italic", 32))
l.pack()


button1 =Button(main_window,text="Start",command=start)
button1.config(width=20,height=2)
button1.pack()


