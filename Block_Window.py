from tkinter import *
from PIL import Image, ImageTk
import main
import admin_options as ao

from tkinter import messagebox

class BlockUser:

    def __init__(self, admin_id):

        self.panel=Tk()
        self.ad_id=admin_id

        self.w = int(self.panel.winfo_screenwidth()*0.6)
        self.h = int(self.panel.winfo_screenheight()*0.6)

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Block Malicious User")
        self.panel.resizable(height=False,width=False)

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)

        self.canvas.create_text(self.xp(50), self.yp(7), text="Enter Email ID of User" ,fill="#3B496F", font=('Candara', self.yp(8), "bold"), anchor='center')
        
        self.canvas.create_text(self.xp(15), self.yp(42), text="E-mail" ,fill="#23304E", font=('Candara', self.yp(6.5), "bold"), anchor='nw')
        self.email=StringVar(self.canvas)
        self.email_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(4.63)), textvariable=self.email)
        self.email_field.place(x=self.xp(40), y=self.yp(42))


        img = Image.open("C:\\Users\\HP\\Desktop\\OpenSpeech\\submit.png")
        img = img.resize((self.xp(20), self.yp(10)), Image.ANTIALIAS)
        self.block_btn=Button(self.canvas, text="Block", command=self.block)#'''image=ImageTk.PhotoImage(img),'''
        self.block_btn.place(x=self.xp(40), y=self.yp(55))

        img = Image.open("C:\\Users\HP\\Desktop\\OpenSpeech\\submit.png")
        img = img.resize((self.xp(20), self.yp(10)), Image.ANTIALIAS)
        self.unblock_btn=Button(self.canvas, text="UnBlock", command=self.unblock)#'''image=ImageTk.PhotoImage(img),'''
        self.unblock_btn.place(x=self.xp(90), y=self.yp(55))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)
        
    def block(self):

        data=(self.email.get())
        main.block_user(data)
        self.panel.destroy()
        d=ao.AdminNavigationPanel(self.ad_id)

    def unblock(self):

        data=(self.email.get())
        main.unblock_user(data)
        self.panel.destroy()
        d=ao.AdminNavigationPanel(self.ad_id)
