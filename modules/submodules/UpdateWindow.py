from tkinter import Frame, Label, Entry, Button, StringVar
from sqlite3 import connect
from os import path, pardir

class UpdateWindow(Frame):

    def __init__(self, master=None, dbPath=None, cName=None):

        super().__init__(master=master)
        self.master = master
        self.master.title("Update contact")
        self.master.geometry("+700+200")
        self.dbPath = path.join(path.dirname(__file__), pardir, pardir, 'contacts.db')
        self.refName = cName

        self.nameLabel = Label(master=self, text="Name: ")
        self.nameLabel.grid(row=0, column=0, padx=10, pady=10)

        self.nameValue = Label(master=self)
        self.nameValue.grid(row=0, column=1, padx=10, pady=10)

        self.phoneLabel = Label(master=self, text="Phone: ")
        self.phoneLabel.grid(row=1, column=0, padx=10, pady=10)

        self.phoneValue = Entry(master=self)
        self.phoneValue.grid(row=1, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.emailLabel = Label(master=self, text="Email: ")
        self.emailLabel.grid(row=2, column=0, padx=10, pady=10)

        self.emailValue = Entry(master=self)
        self.emailValue.grid(row=2, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.addressLabel = Label(master=self, text="Address: ")
        self.addressLabel.grid(row=3, column=0, padx=10, pady=10)

        self.addressValue = Entry(master=self)
        self.addressValue.grid(row=3, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        self.submit = Button(master=self, text="Submit", command=self.updateDB)
        self.submit.grid(row=4, columnspan=2, padx=10, pady=10)

        self.repaint()

        self.pack()

    def updateDB(self):

        try:
            with connect(self.dbPath) as conn:
                cursor = conn.cursor()
                data = cursor.execute(f"UPDATE contacts SET phone=?, email=?, address=? WHERE name LIKE '%{str(self.nameValue.cget('text'))}%'", (int(self.phoneValue.get()), str(self.emailValue.get()), str(self.addressValue.get())))
                self.master.destroy()
        except:
            raise Exception("Error occured while updating data")

    def repaint(self):

        try:
            with connect(self.dbPath) as conn:
                cursor = conn.cursor()
                valueStore = cursor.execute(f"SELECT * FROM contacts WHERE name LIKE '%{str(self.refName)}%'").fetchall()[0]
                print(valueStore)
                self.nameValue.config(text=valueStore[1])
                self.phoneValue.insert('end', valueStore[2])
                self.emailValue.insert('end', valueStore[3])
                self.addressValue.insert('end', valueStore[4])
        except:
            print("Error occured in update window module")