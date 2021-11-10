from utils import *

def draw_list(list, window, canvas, pointer = -1, done = False):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(list) + 1)
    offset = 4
    spacing = 2
    normalised_list = [i / max(list) for i in list]

    for i, height in enumerate(normalised_list):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        if i == pointer:
            colour = red
        elif done == True:
            colour = green
        else:
            colour = gray
        canvas.create_rectangle(x0, y0, x1, y1, fill=colour)

    window.update_idletasks()