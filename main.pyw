
from tkinter import *

WIDTH = 800
HEIGHT = 300
BG = 'lightgray'
TITLE = 'Graphic EQ'


slider_and_label_count = 0

class Slider_and_label:

    def __init__(self, window, from_=0, to=0, text=''):
        global slider_and_label_count
        slider_and_label_count += 1
        self.count = slider_and_label_count


        self.label = Label(window, text=text)
        self.scale = Scale(window, from_=from_, to=to)

    def place(self):
        global slider_and_label_count

        x_pos_constant = -15

        x_pos = (self.count/(slider_and_label_count+1))*WIDTH + x_pos_constant
        y_pos = HEIGHT-150
        print(x_pos)

        self.label.place(x=x_pos, y=y_pos)
        self.scale.place(x=x_pos, y=y_pos+30)
        




# declare the window
window = Tk()

window.configure(width=WIDTH, height=HEIGHT, bg=BG)



window.title(TITLE)








window.configure()

w1 = Slider_and_label(window, from_=100, to=0, text='30hz')
w2 = Slider_and_label(window, from_=100, to=0, text='100hz')
w1.place()
w2.place()

mainloop()
