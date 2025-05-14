from tkinter import *

window = None
canvas = None
WIDTH, HEIGHT = 512, 512

window = Tk()
window.title("show window")
canvas = Canvas(window, width=WIDTH, height=HEIGHT)

def load_image(fname):
    global WIDTH, HEIGHT
    input_image = []

    with open(fname, "rb") as file_path:
        for i in range(0, HEIGHT):
            temp_list = []
            for j in range(0, WIDTH):
                data_R = int.from_bytes(file_path.read(1), "little")
                data_G = int.from_bytes(file_path.read(1), "little")
                data_B = int.from_bytes(file_path.read(1), "little")
                
                temp_tuple = (data_R, data_G, data_B)
                temp_list.append(temp_tuple)
                
            input_image.append(temp_list)

    return input_image

def draw_image(image):
    global WIDTH, HEIGHT
    rgb_string = ""

    for i in range(0, HEIGHT):
        temp_string = ""
        for j in range(0, WIDTH):
            data = image[i][j]
            temp_string += f"#{data[0]:02x}{data[1]:02x}{data[2]:02x} "
        rgb_string += "{" + temp_string + "} "
    paper.put(rgb_string)

paper = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH//2, HEIGHT//2), image=paper, state="normal")

draw_image(load_image("testfilefolder\data4.raw"))

canvas.pack()
window.mainloop()