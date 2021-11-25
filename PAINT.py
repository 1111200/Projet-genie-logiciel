from fileinput import filename
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Scale
from tkinter import colorchooser
from tkinter import filedialog 
#from PIL.ImageGrab import ImageGrab

class Paint():
    def __init__(self,root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("800x520")
        self.root.configure(background='white')
        self.root.resizable(0,0)


        self.pen_color ="black"
        self.eraser_color = "white"


        #ajout de widgets à la fenêtre tkinter
        self.color_frame = LabelFrame(self.root, text='Color', font=('arial',15),bd=5,relief=RIDGE, bg='white')
        self.color_frame.place(x=0, y=0, width=70, height=185)
        colors = ('#ff0000','#ff4dd2','#ffff33','#000000','#0066ff','#660033','#4dff4d','#b300b3','#00ffff','#808080','#99ffcc','#336600','#ff9966','#ff99ff','#00cc99',)
        i = j = 0
        for color in colors:
            Button(self.color_frame, bg=color, bd=2, relief=RIDGE, width=3, command=lambda col =color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1

        self.eraser_button = Button(self.root, text='ERASER',bd=4,bg='white',command=self.eraser,width=8,relief=RIDGE)
        self.eraser_button.place(x=0,y=187)

        self.clear_button = Button(self.root, text='Clear',bd=4,bg='white',command=lambda : self.canvas.delete("all"),width=8,relief=RIDGE)
        self.clear_button.place(x=0,y=217)

        self.save_button = Button(self.root, text='Save',bd=4,bg='white',command=self.Enr,width=8,relief=RIDGE)
        self.save_button.place(x=0,y=247)

        self.canvas_color_button = Button(self.root, text='Canvas',bd=4,bg='white',command=self.canvas_color,width=8,relief=RIDGE)
        self.canvas_color_button.place(x=0,y=277)

        #créer une échelle pour la taille du stylo et de la gomme
        self.pen_size_scale_frame = LabelFrame(self.root, text="size",bd=5, bg='white',font=('arial',15,'bold'),relief=RIDGE)
        self.pen_size_scale_frame.place(x=0,y=320, height=200,width=70)

        self.pen_size = Scale(self.pen_size_scale_frame, orient=VERTICAL, from_= 50,to=0,length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1, padx=15)

        #toile de fond...
        self.canvas = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=500, width=700)
        self.canvas.place(x=80,y=0) 

        #bind the canvas with mouse drag
        self.canvas.bind('<B1-Motion>', self.paint)


    #functions are defined here
    def paint(self,event):
        x1,y1 = (event.x-2),(event.y - 2)
        x2,y2 = (event.x+2),(event.y + 2)

        self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.pen_size.get())


    def select_color(self,col):
        self.pen_color = col 


    def eraser(self):
        self.pen_color = self.eraser_color

    def canvas_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]


    def Enr(self):
        try:
            filename =filedialog.asksaveasfilename(defaultextension='.jpg')
            print(filename)
            x=self.root.winfo_rootx() + self.canvas.winfo_x()
            print(x, self.canvas.winfo_x())

            y=self.root.winfo_rooty() + self.canvas.winfo_y()
            print(y)

            x1 = x + self.canvas.winfo_width()
            print(x1)

            y1 = y + self.canvas.winfo_height()
            print(y1)

            #ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
            messagebox.showinfo('print says', 'image is saved as' + str(filename))

        except:
            print("not saved some thing went wrong")

if __name__=="__main__":
    import tkinter as tk
    root = tk.Tk()
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='python/apple-icon-144x144.png'))   
    p = Paint(root)
    root.mainloop()