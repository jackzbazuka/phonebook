from tkinter import Frame, Label

class Ewin(Frame):

    def __init__(self, master=None, warnMsg=None, **kw):

        super().__init__(master=master, **kw)
        self.master = master
        self.master.resizable(False, False)
        self.master.geometry('+700+200')
        self.master.title('Error')

        self.ewarn = Label(master=self.master, text=warnMsg, fg="#d10000")
        self.ewarn.grid(row=0, column=0, padx=20, pady=40)