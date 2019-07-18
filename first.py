from tkinter import *
from PIL import Image, ImageTk
import login_panel as lp
import signup_panel as sp

class FirstPanel:

    def __init__(self):

        self.panel=Tk()

        self.w = self.panel.winfo_screenwidth()
        self.h = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Welcome User!!")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)
        
        self.lady=ImageTk.PhotoImage(file="lady.png")
        self.canvas.create_image(self.xp(61.8), self.yp(2.31), anchor='nw', image=self.lady)

        self.login_pic=ImageTk.PhotoImage(file="login.png")
        self.signup_pic=ImageTk.PhotoImage(file="signup.png")

        self.login=Button(self.canvas, image=self.login_pic, command=self.log)
        self.login.place(x=self.xp(13), y=self.yp(46.29))

        self.signup=Button(self.canvas, image=self.signup_pic, command=self.sign)
        self.signup.place(x=self.xp(32.5), y=self.yp(46.29))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)

    def sign(self):
        x=sp.SignupPanel()

    def log(self):
        x=lp.LoginPanel()  

x=FirstPanel()
