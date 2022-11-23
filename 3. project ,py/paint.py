from tkinter import *
import PIL
from PIL import ImageDraw


def save():
    filename = 'image.png'
    image1.save(filename)

def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2), fill='black', width=50)
    #  --- PIL
    draw.line((x1, y1, x2, y2), fill='black', width=50)


root = Tk()

cv = Canvas(root, width=640, height=480, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)
# ---- 
cv.bind('<B1-Motion>', paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()

root.mainloop()

    