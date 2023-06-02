import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

frame = tk.Frame(window, width = 100, height = 100)
frame.pack()
frame.place(anchor = "center", relx = 0.5, rely = 0.5)
hermie = Image.open("Hermie_Crawling.png").convert("RGBA")
cropped_hermie = hermie.crop([0, 0, 32, 32])
revived_hermie = ImageTk.PhotoImage(cropped_hermie)

label = tk.Label(frame, image = revived_hermie)
label.pack()

def hermie_resize(e):
    global revived_hermie
    revived_hermie = Image.open("Hermie_Crawling.png").convert("RGBA")
    resized = revived_hermie.resize((e.width, e.height),     Image.ANTIALIAS)

    HERMSTER2 = ImageTk.PhotoImage(resized)
    label = tk.Label(frame, image=HERMSTER2)
    label.pack()

window.bind("<Configure>", hermie_resize)

#always leave at the bottom
tk.mainloop()