#coding: utf-8
import tkinter as tk
import random as R

#set the first centre location randomly
x=100
y=100
dx=R.randint(1,3)
dy=R.randint(1,3)

#Move Function
def move():
    global x, y, dx, dy
    canvas.create_oval(x-30, y-30, x+30, y+30, fill="white", width=1) #same color as the canvas bg to cancel

    x+=dx  #x=x+dy
    y+=dy   #y=y+dy
    canvas.create_oval(x-30, y-30, x+30, y+30, fill="pink", width=1)

    if x+30 >= canvas.winfo_width():
        dx=-R.randint(1,3)
    if x-30 <= 0:
        dx=+R.randint(1,3)
    if y+30 >= canvas.winfo_height():
        dy=-R.randint(1,3)
    if y-30 <= 0:
        dy=+R.randint(1,3)
    
    frame.after(10, move) #to loop the move function
    


frame = tk.Tk()
frame.geometry("800x800")

canvas=tk.Canvas(frame, width=700, height=700, bg="white")
canvas.place(x=50, y=50)

#Trigger the move function
frame.after(10, move)

frame.mainloop()
