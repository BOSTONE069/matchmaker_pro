import random
import time
from tkinter import Tk , Button , DISABLED

def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first: #This is about defining the logic of the game
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y:
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True





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

for x in range(6): # this loop if for defining the buttons in the chart
    for y in range(4):
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8) #This is for defining the height and width of the buttons
        button.grid(column = x, row = y)
        buttons[x,y] = button # this is for storing the buttons in the buttons at line eleven
        button_symbols[x,y] = symbols.pop()

win.mainloop()
