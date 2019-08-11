from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,filedialog
import main
import admin_options as ao

from tkinter import messagebox

class AddTheme:

    def __init__(self, admin_id):

        self.panel=Tk()
        self.ad_id=admin_id
        self.w = int(self.panel.winfo_screenwidth())
        self.h = int(self.panel.winfo_screenheight())

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Add New Admin")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg1=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg1)

        self.canvas.create_text(self.xp(50), self.yp(7), text="Add Theme Parameters" ,fill="#3B496F", font=('Candara', self.yp(6), "bold"), anchor='center')

        self.canvas.create_text(self.xp(10), self.yp(17), text="Weather" ,fill="#23304E", font=('Candara', self.yp(4.5), "bold"), anchor='nw')
        self.weather=StringVar(self.canvas)
        self.weather_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(2.5)), textvariable=self.weather)
        self.weather_field.place(x=self.xp(40), y=self.yp(18))
        
        self.canvas.create_text(self.xp(10), self.yp(23), text="Background Image" ,fill="#23304E", font=('Candara', self.yp(4.5), "bold"), anchor='nw')
        self.bckg=StringVar(self.canvas)
        self.bckg_btn=Button(self.w, text="Select Background Picture", fg="#384E7E", command=self.insert_bckg, font=('Candara', self.yp(2.5), "bold"))
        self.bckg_btn.place(x=self.xp(40), y=self.yp(23))
        
        h=0
        for i in range(1, 8):
            
            self.canvas.create_text(self.xp(10), self.yp(29+h), text="Canvas"+i+" Image" ,fill="#23304E", font=('Candara', self.yp(4.5), "bold"), anchor='nw')
            self.canvas.create_text(self.xp(10), self.yp(29+h), text="Canvas"+i+" Image" ,fill="#23304E", font=('Candara', self.yp(4.5), "bold"), anchor='nw')  
            globals()["c"+str(i)]=StringVar(self.canvas)
            globals()["c"+str(i)+"_btn"]=Button(self.w, text="Select Picture", fg="#384E7E", command=self.insert_pic(i), font=('Candara', self.yp(2.5), "bold"))
            globals()["c"+str(i)+"_btn"].place(x=self.xp(40), y=self.yp(29))
            h=h+6

        self.canvas.create_text(self.xp(10), self.yp(71), text="Font Colour" ,fill="#23304E", font=('Candara', self.yp(4.5), "bold"), anchor='nw')  
        self.font=StringVar(self.canvas)
        self.font_field=Entry(self.panel, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(2.5)), textvariable=self.font)
        self.font_field.place(x=self.xp(40), y=self.yp(72))

        img = Image.open("C:\\Users\\HP\\Desktop\\OpenSpeech\\submit.png")
        img = img.resize((self.xp(20), self.yp(6)), Image.ANTIALIAS)
        self.submit_btn=Button(self.canvas, text="Submit", command=self.submit)#'''image=ImageTk.PhotoImage(img),'''
        self.submit_btn.place(x=self.xp(40), y=self.yp(80))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)
        
    def submit(self):

        data=(self.weather, self.bckg, globals()["c1"], globals()["c2"], globals()["c3"], globals()["c4"], globals()["c5"], globals()["c6"], globals()["c7"], self.font)
        main.add_theme(data)
        self.panel.destroy()
        d=ao.AdminNavigationPanel(self.ad_id)

    def insert_bckg(self):
        self.bckg=filedialog.askopenfilename(title="Select a Background Picture")

    def insert_pic(self, i):
        globals()["c"+str(i)]= filedialog.askopenfilename(title="Select Canvas"+i+" Picture")

if __name__=="__main__":
    d = AddTheme(1)
