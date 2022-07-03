import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

def paint():
    pass

def add_image():
    pass

# open window with instructions what to do
def get_info(main):

    # define window and frame sizes
    WINSIZE = [600,600]
    FRAMESIZE = [400,300]
    # create window
    window = tk.Tk()
    window.geometry("x".join(str(size) for size in WINSIZE))
    window.resizable(False, False)
    window.title("Info")
    
    # create frame for buttons
    frame = tk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor="c", width=FRAMESIZE[0])

    '''create buttons'''
    
    paintBut = tk.Button(
            frame,
            text="How to paint",
            bd=5,
            command=lambda: info("paint")
    )

    galleryBut = tk.Button(
            frame,
            text="What is gallery",
            bd=5,
            command=lambda: info("gallery")
    )

    addBut = tk.Button(
            frame,
            text="How to add images to the gallery",
            bd=5,
            command=lambda: info("add")
    )
    
    filtersBut = tk.Button(
            frame,
            text="How to add filters",
            bd=5,
            command=lambda: info("filter")
    )
    
    exitBut = tk.Button(
            frame,
            text="Return to the main window",
            bd=5,
            command=lambda: [window.destroy(), main()]
    )
    
    # pack all buttons
    paintBut.pack(expand=True, fill="x", side="top")
    galleryBut.pack(expand=True, fill="x", side="top")
    addBut.pack(expand=True, fill="x", side="top")
    filtersBut.pack(expand=True, fill="x", side="top")
    exitBut.pack(expand=True, fill="x", side="top")

    window.mainloop()

def info(key):
    pass

def add_filter():
    pass

def show_gallery():
    pass

