from tkinter import Tk, Frame
from sqlite3 import connect
from os import path
from modules.ListModule import ListModule

class MainInterface(Frame):

    def __init__(self, master=None, **kw):

        super().__init__(master=master, **kw)
        self.master = master
        self.master.title('Phonebook')
        self.master.resizable(False, False)
        self.master.geometry('+500+200')

        self.list_module = ListModule(master=self.master)
        self.list_module.grid(row=0, column=0, padx=10, pady=10)

open('contacts.db', 'a').close()

FILEPATH = path.join(path.dirname(__file__), 'contacts.db')

try:
    with connect(FILEPATH) as conn:
        query = '''CREATE TABLE IF NOT EXISTS contacts (uid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone INTEGER NOT NULL, email TEXT, address TEXT)'''
        cursor = conn.cursor()
        cursor.execute(query)
        print('Database created successfully')
except:
    print('Database creation failed')

if __name__ == "__main__":
    root = Tk()
    pb = MainInterface(master=root)
    root.mainloop()