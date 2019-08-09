from tkinter import *
from PIL import Image, ImageTk
import main
from tkinter import messagebox

class SignupPanel:

    def __init__(self):

        self.panel=Toplevel()

        self.w = self.panel.winfo_screenwidth()
        self.h = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Registration Page")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)
        
        self.lady=ImageTk.PhotoImage(file="lady.png")
        self.canvas.create_image(self.xp(61.8), self.yp(2.31), anchor='nw', image=self.lady)

        self.avatar=ImageTk.PhotoImage(file="avatar.png")
        self.canvas.create_image(self.xp(27.4), self.yp(3.5), anchor='nw', image=self.avatar)

        self.canvas.create_text(self.xp(10), self.yp(32), text="Name" ,fill="#23304E", font=('Candara', self.yp(3.5), "bold"), anchor='nw')
        self.name=StringVar(self.canvas)
        self.name_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(3.5)), textvariable=self.name)
        self.name_field.place(x=self.xp(25), y=self.yp(32))

        self.canvas.create_text(self.xp(10), self.yp(40), text="E-mail" ,fill="#23304E", font=('Candara', self.yp(3.5), "bold"), anchor='nw')
        self.email=StringVar(self.canvas)
        self.email_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(3.5)), textvariable=self.email)
        self.email_field.place(x=self.xp(25), y=self.yp(40))

        self.canvas.create_text(self.xp(10), self.yp(48), text="Password" ,fill="#23304E", font=('Candara', self.yp(3.5), "bold"), anchor='nw')  
        self.password=StringVar(self.canvas)
        self.pass_field=Entry(self.panel, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(3.5)), textvariable=self.password)
        self.pass_field.place(x=self.xp(25), y=self.yp(48))

        self.canvas.create_text(self.xp(10), self.yp(56), text="Phone No." ,fill="#23304E", font=('Candara', self.yp(3.5), "bold"), anchor='nw')
        self.phone=StringVar(self.canvas)
        self.phone_field=Entry(self.panel, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(3.5)), textvariable=self.phone)
        self.phone_field.place(x=self.xp(25), y=self.yp(56))

        self.canvas.create_text(self.xp(10), self.yp(64), text="City" ,fill="#23304E", font=('Candara', self.yp(3.5), "bold"), anchor='nw')
        self.city=StringVar(self.canvas)
        self.city_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(3.5)), textvariable=self.city)
        self.city_field.place(x=self.xp(25), y=self.yp(64))

        self.signup_pic=ImageTk.PhotoImage(file="signup.png")
        self.signup=Button(self.canvas, image=self.signup_pic, command=self.sign)
        self.signup.place(x=self.xp(26), y=self.yp(74))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)
        
    def sign(self):

        data=(self.name.get(), self.city.get(), self.email.get(), self.password.get(), self.phone.get(), True)
        if self.name.get()=="" or self.city.get()=="" or self.email.get()=="" or self.password.get()=="":
            self.canvas.create_text(self.xp(5), self.yp(70), text="*Incorrect Username or Password" ,fill="#9F233A", font=('Candara', self.yp(5), "bold"), anchor='nw')
        else:
            messagebox.showinfo("Successful", "User Registered")
            main.add_user(data)
            self.name.set("")
            self.city.set("")
            self.email.set("")
            self.password.set("")
            self.phone.set("")
            self.panel.destroy()
        
        
     
       

        
