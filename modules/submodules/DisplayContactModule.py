from tkinter import Frame, Label
from os import path, pardir
from sqlite3 import connect

class DisplayContactModule(Frame):

    def __init__(self, master=None, info=None, **kw):

        super().__init__(master=master, **kw)
        self.master = master
        self.master.title('Contact Information')
        self.master.resizable(False, False)
        self.master.geometry('+700+200')
        self.db_path = path.join(path.dirname(__file__), pardir, pardir, 'contacts.db')

        try:
            with connect(self.db_path) as conn:
                cursor = conn.cursor()
                query = f"SELECT * from contacts WHERE name LIKE '%{info}%'"
                response = cursor.execute(query).fetchall()
                #print(response)

        except:
            self.master.destroy()

        self.nameLabel = Label(master=self.master, text='Name:', anchor='w')
        self.nameLabel.grid(row=0, column=0, padx=30, pady=20)

        self.nameValue = Label(master=self.master, text=response[0][1], anchor='w')
        self.nameValue.grid(row=0, column=1, padx=30, pady=20)

        self.phoneLabel = Label(master=self.master, text='Phone:', anchor='w')
        self.phoneLabel.grid(row=1, column=0, padx=30, pady=20)

        self.phoneValue = Label(master=self.master, text=str(response[0][2]), anchor='w')
        self.phoneValue.grid(row=1, column=1, padx=30, pady=20)

        self.emailLabel = Label(master=self.master, text='Email:', anchor='w')
        self.emailLabel.grid(row=2, column=0, padx=30, pady=20)

        self.emailValue = Label(master=self.master, text=response[0][3], anchor='w')
        self.emailValue.grid(row=2, column=1, padx=30, pady=20)

        self.addressLabel = Label(master=self.master, text='Address:', anchor='w')
        self.addressLabel.grid(row=3, column=0, padx=30, pady=20)

        self.addressValue = Label(master=self.master, text=response[0][4], anchor='w')
        self.addressValue.grid(row=3, column=1, padx=30, pady=20)