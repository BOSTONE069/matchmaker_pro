import random
import time
from tkinter import Tk , Button , DISABLED

win = Tk()
win.title('Matchmaker') #this is the title of the match maker
win.resizable(width=False, height=False) #This makes the window to be fixed
first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u270C',u'\u270F',
          u'\u2712',u'\u2714',u'\u2716',u'\u2728',u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u270C',u'\u270F',
                        u'\u2712',u'\u2714',u'\u2716',u'\u2728'] #This is to iclude the symbols in the game programs

random.shuffle(symbols)


win.mainloop()
