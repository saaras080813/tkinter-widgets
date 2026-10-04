from tkinter import TK, Label, Button, Frame, messagebox
from PIL import Image, ImageTk

# window
window = Tk()
window.title("My Photo Album")
window.geometry("450x550")


# frame 
frame = Frame(window)
frame.pack(fill="both", expand=True)

# label
title = Label(frame, text="My photo album", width=100, bg="violet", fg="white")
title.pack(pady=10)
img_file = Image.open("cute_puppies.jpg")
img_file = img_file.resize((400, 300))
photo = ImageTk.PhotoImage(img_file)
pic = Label(frame, image=photo)
pic.pack(pady=10)

def show_reaction():
    messagebox.showinfo("Reaction", "Guli Guli Guli!!!")

def show_details():
    messagebox.showwarning("Details", "Cute Little Labra puppies")

react_btn = Button(frame, text="Click to react", bg="blue", fg="white",command=show_reaction)
react_btn.pack(pady=5)

details_btn = Button(frame, text="See Details", bg="blue", fg="white",command=show_details)
details_btn.pack(pady=5)

window.mainloop()
