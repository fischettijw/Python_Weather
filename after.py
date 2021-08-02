import tkinter as tk
import os
import time
os.system('cls')


def prt(sec):
    print(f'prt: {sec}')
    # time.sleep(1)


def end(sec):
    print(f'end: {sec}')
    win.destroy()


win = tk.Tk()
win.geometry('400x600+1000+300')
win.after(8000, lambda: end(8000))
win.after(3000, lambda: prt(3000))
win.after(3000, lambda: prt(3000))
win.after(3000, lambda: prt(3000))
win.after(3000, lambda: prt(3000))
win.after(3000, lambda: prt(3000))

print('after')

win.mainloop()
