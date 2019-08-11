from tkinter import *
from PIL import Image, ImageTk
import main
import navigation_pane as np
import AdminProfileEdit as ape
import UserSearchedKeywords as usk
import NewAdmin
import ThemePanel as tp
import Block_Window as bw

from tkinter import messagebox

class AdminNavigationPanel:

    def __init__(self, admin_id):

        self.panel=Tk()

        self.w = int(self.panel.winfo_screenwidth()*0.6)
        self.h = int(self.panel.winfo_screenheight()*0.6)

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Admin Options Page")
        self.panel.resizable(height=False,width=False)

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="upanelbckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)

        self.ad_id=admin_id

        self.change_admin_settings=Button(self.canvas, text="Edit Profile", command=self.edit, anchor="center")
        self.change_admin_settings.place(x=self.xp(50), y=self.yp(10))

        self.add_admin=Button(self.canvas, text="Add an Admin", command=self.new_admin, anchor="center")
        self.add_admin.place(x=self.xp(50), y=self.yp(25))

        self.add_app=Button(self.canvas, text="Add an Application", command=self.new_app, anchor="center")
        self.add_app.place(x=self.xp(50), y=self.yp(40))

        self.see_searches=Button(self.canvas, text="See Unfound Searche Keywords", command=self.search, anchor="center")
        self.see_searches.place(x=self.xp(50), y=self.yp(55))

        self.block_btn=Button(self.canvas, text="Block a Malicious User", command=self.block, anchor="center")
        self.block_btn.place(x=self.xp(50), y=self.yp(70))

        self.theme_btn=Button(self.canvas, text="Add a Theme", command=self.theme, anchor="center")
        self.theme_btn.place(x=self.xp(50), y=self.yp(85))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)
        
    def edit(self):
        self.panel.destroy()
        d=ape.AdminEdit(self.ad_id)

    def new_admin(self):
        self.panel.destroy()
        d = NewAdmin.AddAdmin(self.ad_id)

    def new_app(self):
        self.panel.destroy()
        #d = add_App(self.ad_id)

    def search(self):
        d=usk.SearchedKeywords()

    def block(self):
        self.panel.destroy()
        d=bw.BlockUser(self.ad_id)
        
    def theme(self):
        self.panel.destroy()
        d=tp.AddTheme(self.ad_id)
