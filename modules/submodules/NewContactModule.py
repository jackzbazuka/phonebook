from tkinter import Frame, Entry, Label, Button, Tk, StringVar
from sqlite3 import connect
from os import path, pardir
from modules.submodules.Ewin import Ewin

class NewContactModule(Frame):

    def __init__(self, master=None, **kw):

        super().__init__(master=master, **kw)
        self.master = master
        self.master.title('New Contact')
        self.master.resizable(False, False)
        self.master.geometry('+600+200')
        self.db_path = path.join(path.dirname(__file__), pardir, pardir, 'contacts.db')

        self.nameStore = StringVar()
        self.phoneStore = StringVar()
        self.emailStore = StringVar()
        self.addressStore = StringVar()

        self.nameLabel = Label(master=self.master, text='Name', anchor='w')
        self.nameLabel.grid(row=0, column=0, padx=10, pady=10)

        self.nameEntry = Entry(master=self.master, textvariable=self.nameStore, width=50)
        self.nameEntry.grid(row=0, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.phoneLabel = Label(master=self.master, text='Phone', anchor='w')
        self.phoneLabel.grid(row=1, column=0, padx=10, pady=10)

        self.phoneEntry = Entry(master=self.master, textvariable=self.phoneStore, width=50)
        self.phoneEntry.grid(row=1, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.emailLabel = Label(master=self.master, text='Email', anchor='w')
        self.emailLabel.grid(row=2, column=0, padx=10, pady=10)

        self.emailEntry = Entry(master=self.master, textvariable=self.emailStore, width=50)
        self.emailEntry.grid(row=2, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.addressLabel = Label(master=self.master, text='Address', anchor='w')
        self.addressLabel.grid(row=3, column=0, padx=10, pady=10)

        self.addressEntry = Entry(master=self.master, textvariable=self.addressStore, width=50)
        self.addressEntry.grid(row=3, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.submitButton = Button(master=self.master, text='Submit', command=self.submitData)
        self.submitButton.grid(row=4, columnspan=2, padx=10, pady=10, ipadx=4, ipady=4)

    def submitData(self):

        try:
            if((len(self.addressEntry.get()) == 0) or (len(self.nameEntry.get()) == 0) or (len(self.phoneEntry.get()) == 0) or (len(self.emailEntry.get()) == 0)):
                kite = Tk()
                chi = Ewin(master=kite, warnMsg="Some field(s) might be empty")
                kite.after(2000, lambda: kite.destroy())
                kite.mainloop()

            else:
                with connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    values = (str(self.nameEntry.get()), int(self.phoneEntry.get()), str(self.emailEntry.get()), str(self.addressEntry.get()))
                    query = 'INSERT INTO contacts (name, phone, email, address) VALUES (?,?,?,?)'
                    cursor.execute(query, values)
                    conn.commit()
                    self.confirm()

        except ValueError:
            kite = Tk()
            chi = Ewin(master=kite, warnMsg="Inappropriate value provided")
            kite.after(2000, lambda: kite.destroy())
            kite.mainloop()

        except:
            print('ERROR connecting to database!!!')

    def confirm(self):

        self.p = Tk()
        self.con = Frame(master=self.p)
        self.p.title('Confirm')
        self.p.geometry('+700+200')
        self.p.resizable(False, False)

        self.con = Label(master=self.p, text='Do more entries?')
        self.con.grid(row=0, column=0, columnspan=4, padx=20, pady=30)

        self.by = Button(master=self.p, text='Yes', command=self.refresh)
        self.by.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

        self.bn = Button(master=self.p, text='No', command=self.destroyAll)
        self.bn.grid(row=1, column=1, columnspan=2, padx=20, pady=30)

    def destroyAll(self):

        self.p.destroy()
        self.master.destroy()

    def refresh(self):

        self.nameEntry.delete(0, 'end')
        self.phoneEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.addressEntry.delete(0, 'end')
        self.p.destroy()
