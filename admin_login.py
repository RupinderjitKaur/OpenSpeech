from tkinter import *
from PIL import Image, ImageTk
import main
import admin_options as ao

from tkinter import messagebox

class AdminPanel:

    def __init__(self):

        self.panel=Tk()

        self.w = int(self.panel.winfo_screenwidth()*0.6)
        self.h = int(self.panel.winfo_screenheight()*0.6)

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Admin Login Page")
        self.panel.resizable(height=False,width=False)

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)

        self.canvas.create_text(self.xp(50), self.yp(7), text="Please Enter Your Credentials" ,fill="#3B496F", font=('Candara', self.yp(8), "bold"), anchor='center')

        self.canvas.create_text(self.xp(15), self.yp(31.25), text="E-mail" ,fill="#23304E", font=('Candara', self.yp(6.5), "bold"), anchor='nw')
        self.email=StringVar(self.canvas)
        self.email_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(4.63)), textvariable=self.email)
        self.email_field.place(x=self.xp(40), y=self.yp(31.25))

        self.canvas.create_text(self.xp(15), self.yp(42), text="Password" ,fill="#23304E", font=('Candara', self.yp(6.5), "bold"), anchor='nw')  
        self.password=StringVar(self.canvas)
        self.pass_field=Entry(self.panel, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(4.63)), textvariable=self.password)
        self.pass_field.place(x=self.xp(40), y=self.yp(42))

        #img = Image.open("C:\\Users\\HP\\Desktop\\OpenSpeech\\login.png")
        #img = img.resize((self.xp(20), self.yp(10)), Image.ANTIALIAS)
        self.login=Button(self.canvas, text="Submit", command=self.log)#'''image=ImageTk.PhotoImage(img),'''
        self.login.place(x=self.xp(40), y=self.yp(60))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)
        
    def log(self):

        data=(self.email.get(),self.password.get())
        result=main.verify_admin(data)
        if result is not None:
            self.panel.destroy()
            d = ao.AdminNavigationPanel(result)
        else:
            self.canvas.create_text(self.xp(5), self.yp(70), text="*Incorrect Username or Password" ,fill="#9F233A", font=('Candara', self.yp(5), "bold"), anchor='nw')

if __name__=="__main__":
    d = AdminPanel()
