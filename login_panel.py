from tkinter import *
from PIL import Image, ImageTk
import main
import navigation_pane as np

from tkinter import messagebox

class LoginPanel:

    def __init__(self):

        self.panel=Tk()

        self.w = self.panel.winfo_screenwidth()
        self.h = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Login Page")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)
        
        self.lady=ImageTk.PhotoImage(file="lady.png")
        self.canvas.create_image(self.xp(61.8), self.yp(2.31), anchor='nw', image=self.lady)

        self.canvas.create_text(self.xp(3.25), self.yp(6.95), text="Please Enter Your Credentials" ,fill="#3B496F", font=('Candara', self.yp(6.95), "bold"), anchor='nw')

        self.canvas.create_text(self.xp(3.9), self.yp(31.25), text="E-mail" ,fill="#23304E", font=('Candara', self.yp(4.63), "bold"), anchor='nw')
        self.email=StringVar(self.canvas)
        self.email_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(4.63)), textvariable=self.email)
        self.email_field.place(x=self.xp(19.5), y=self.yp(31.25))

        self.canvas.create_text(self.xp(3.9), self.yp(40.51), text="Password" ,fill="#23304E", font=('Candara', self.yp(4.63), "bold"), anchor='nw')  
        self.password=StringVar(self.canvas)
        self.pass_field=Entry(self.panel, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(4.63)), textvariable=self.password)
        self.pass_field.place(x=self.xp(19.5), y=self.yp(40.51))

        self.login_pic=ImageTk.PhotoImage(file="login.png")
        self.login=Button(self.canvas, image=self.login_pic, command=self.log)
        self.login.place(x=self.xp(27.35), y=self.yp(55.5))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)
        
    def log(self):

        data=(self.email.get(),self.password.get())
        result=main.verify(data)
        if result=='false':
            self.canvas.create_text(self.xp(5), self.yp(70), text="*You have been Blocked" ,fill="#9F233A", font=('Candara', self.yp(5), "bold"), anchor='nw')
        if result is not None:
            main.user = result
            self.panel.destroy()
            d = np.NavigationPanel()
        else:
            self.canvas.create_text(self.xp(5), self.yp(70), text="*Incorrect Username or Password" ,fill="#9F233A", font=('Candara', self.yp(5), "bold"), anchor='nw')

if __name__=="__main__":
    d = LoginPanel()
