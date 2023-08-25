import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Hermie Adventures")
window.geometry("600x600")

window_width = 600
window_height = 600


class Instant_Frame_Probably(tk.Frame):
    def __init__(self, master, photo):
        tk.Frame.__init__(self, master)

        self.image = Image.open(photo).convert("RGBA")

        width, height = self.image.size
        self.left = 0
        self.upper = 0
        lower = height
        right = width/2

        cropped_image = self.image.crop([self.left, self.upper, right, lower])
        self.revived_hermie = cropped_image.copy()
        self.background_image = ImageTk.PhotoImage(cropped_image)

        self.background = tk.Label(self, image = self.background_image)
        self.background.pack(fill = tk.BOTH, expand=tk.YES)
        #window.bind("<Up>", self.jump)
        overall_hermster_size = (int(32 * 4), int(32 * 4))
        self.image = self.revived_hermie.resize((overall_hermster_size))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

        self.x = 0
        self.y = 0
        self.hermie_canvas = tk.Canvas(window, width=32, height=32)
        self.hermie_canvas.pack()
        self.moving_hermie = self.hermie_canvas.create_image(self.x, self.y, anchor=tk.SW, image = self.background_image)

    def Instant_Crop_Lol(self):
        pass

def jump(event):
    global window_height
    global window_width
    global e
    global window
    #self.y = 20
   # self.hermie_canvas.move(self.moving_hermie, self.x, self.y)
   # self.
  #  print(self.hermie_canvas.move)
    window_height = window.winfo_height()/2
    '''for i in range(100):
     time.sleep(0.05)
     e.place(x = window.winfo_width()/2 - 100, y = window_height - i)
     print(window_height - i)'''
    if window_height > 200:
        window_height -= 10
        e.place(x = window.winfo_width()/2, y = window_height)
        window.after(12,jump)

def resize_window(event):
    global window_width, window_height
    window_width = event.width
    window_height = event.height

e = Instant_Frame_Probably(window, "Hermie_Crawling.png")
e.pack(fill = tk.BOTH, expand = tk.YES)
window.bind("<Up>", jump)
window.bind('<Configure>', resize_window)


window.mainloop()
