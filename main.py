import tkinter as tk
def main():

    # some constants
    ROOTSIZE = [600,600]
    FRAMESIZE = [400,400]

    # create root window and determine it's size and name
    root = tk.Tk()
    root.geometry("x".join(str(size) for size in ROOTSIZE))
    root.resizable(False,False)
    root.title("Pythoshop")
    
    # create and place frame for buttons
    buttFrame = tk.Frame(root)
    buttFrame.place(relx=0.5, rely=0.5, anchor="c", width=FRAMESIZE[0])

    '''create buttons'''

    # paint on the images
    paintBut = tk.Button(
            buttFrame,
            text="Paint",
            bd=5,
            command=paint
    )
    
    # explain what to do
    infoBut = tk.Button(
            buttFrame,
            text="What to do",
            bd=5,
            command=get_info
    )
    
    # show gallery
    gallerBut = tk.Button( 
            buttFrame,
            text="See gallery",
            bd=5,
            command=show_gallery
    )

    # add filter
    filterBut = tk.Button(
            buttFrame,
            text="Add filters",
            bd=5,
            command=add_filter
    )

    # add photo to the gallery
    addBut = tk.Button(
            buttFrame,
            text="Add button",
            bd=5,
            command=add_image
    )

    # pack all buttons
    infoBut.pack(expand=True, fill="x", side="top")
    paintBut.pack(expand=True, fill="x", side="top") 
    gallerBut.pack(expand=True, fill="x", side="top")
    filterBut.pack(expand=True, fill="x", side="top")
    addBut.pack(expand=True, fill="x", side="top")
    
    root.mainloop()

def paint():
    pass

def add_image():
    pass

def get_info():
    pass

def add_filter():
    pass

def show_gallery():
    pass

if __name__ == "__main__":
    main()
