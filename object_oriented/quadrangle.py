import tkinter as tk
import random
import time

class quadrangle:
    def __init__(self, x, y, z, width, height, color):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2, outline=self.color)

window = tk.Tk()
window.title("Quadrangle")

canvas = tk.Canvas(window, width=512, height=512)

canvas.pack()

for i in range (30):
    random_x = random.randint(0, 512)
    random_y = random.randint(0, 512)
    random_width = random.randint(10, 100)
    random_height = random.randint(10, 100)
    random_color = f'#{random.randint(0, 0xFFFFFF):06x}'

    q = quadrangle(random_x, random_y, 0, random_width, random_height, random_color)
    q.draw()
    time.sleep(0.05)
    canvas.update()

window.mainloop()
