import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Hermie Adventures")
window.geometry("600x600")

class Instant_Frame_Probably(tk.Frame):
    def __init__(self, master, photo):
        tk.Frame.__init__(self, master)

        self.image = Image.open(photo).convert("RGBA")

        width, height = self.image.size
        left = 0
        upper = 0
        lower = height
        right = width/2

        cropped_image = self.image.crop([left, upper, right, lower])
        self.revived_hermie = cropped_image.copy()
        self.background_image = ImageTk.PhotoImage(cropped_image)

        self.background = tk.Label(self, image = self.background_image)
        self.background.pack(fill = tk.BOTH, expand=tk.YES)
        self.background.bind('<Configure>', self.resize_hermie)

    def Instant_Crop_Lol(self):
        pass

    def resize_hermie(self, event):
        new_width_hermster = event.width
        new_height_hermster = event.height
        print(event.width, event.height)
        rescaled_width = int(new_width_hermster*0.05)
        rescaled_height = int(new_height_hermster*0.10)
        self.image = self.revived_hermie.resize((rescaled_width, rescaled_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image = self.background_image)


e = Instant_Frame_Probably(window, "Hermie_Crawling.png")
e.pack(fill = tk.BOTH, expand = tk.YES)

window.mainloop()
