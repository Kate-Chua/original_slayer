import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Unslauy")
window.geometry("600x600")

class Instant_Frame_Probably(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.image = Image.open("Hermie_Crawling.png").convert("RGBA")
        self.revived_hermie = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = tk.Label(self, image = self.background_image)
        self.background.pack(fill = tk.BOTH, expand=tk.YES)
        self.background.bind('<Configure>', self.resize_hermie)

    def resize_hermie(self, event):
        new_width_hermster = event.width
        new_height_hermster = event.height
        print(event.width, event.height)
        self.image = self.revived_hermie.resize(new_width_hermster, new_height_hermster)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image = self.background_image)


e = Instant_Frame_Probably(window)
e.pack(fill = tk.BOTH, expand = tk.YES)

window.mainloop()
