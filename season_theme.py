from tkinter import *
from PIL import Image, ImageTk

class ThemePanel:

    def __init__(self):

        self.panel=Tk()

        self.w = self.panel.winfo_screenwidth()
        self.h = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Themes")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="themebckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)
        
        self.sum_pic=ImageTk.PhotoImage(file="sum_icon.png")
        self.aut_pic=ImageTk.PhotoImage(file="aut_icon.png")
        self.rain_pic=ImageTk.PhotoImage(file="rain_icon.png")
        self.win_pic=ImageTk.PhotoImage(file="win_icon.png")

        self.canvas.create_image(self.xp(26), self.yp(10), anchor='nw', image=self.sum_pic)
        self.canvas.create_image(self.xp(26), self.yp(50), anchor='nw', image=self.aut_pic)
        self.canvas.create_image(self.xp(60), self.yp(10), anchor='nw', image=self.rain_pic)
        self.canvas.create_image(self.xp(60), self.yp(50), anchor='nw', image=self.win_pic)

        #use radio buttons
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h) 

x=ThemePanel()
