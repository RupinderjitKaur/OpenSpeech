from tkinter import *
from tkinter.ttk import Treeview as tvw
from PIL import Image, ImageTk
import main
import admin_options as ao

from tkinter import messagebox

class SearchedKeywords:

    def __init__(self):

        self.panel=Toplevel()

        self.w = int(self.panel.winfo_screenwidth()*0.5)
        self.h = int(self.panel.winfo_screenheight()*0.5)

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Searched Unfound Keywords")
        self.panel.resizable(height=False,width=False)
        self.panel.config(bg="white")

        data=main.get_unknown_keywords()

        self.table=tvw(self.panel, columns=("#1", "#2"))
        
        self.table.heading("#0", text="SrNo.")#, font=('Candara', 20, "bold"))
        self.table.heading("#1", text="Keywords")#, font=('MV Boli', 20, "bold"))
        self.table.heading("#2", text="User_ID")#, font=('MV Boli', 20, "bold"))

        self.table.column("#0", width=self.xp(20))
        self.table.column("#1", width=self.xp(40))
        self.table.column("#2", width=self.xp(40))
        
        for i in data :
            self.table.insert('', "end", text=i[0], values=(i[1], i[2]))

        self.table.place(x=0, y=0)
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)

if __name__=="__main__":
    d = SearchedKeywords()
