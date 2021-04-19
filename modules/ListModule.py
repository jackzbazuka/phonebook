from os import path, pardir
from tkinter import Frame, CENTER, Tk, Entry, Scrollbar, Button
from tkinter.ttk import Style, Treeview
from sqlite3 import connect
from modules.submodules.NewContactModule import NewContactModule
from modules.submodules.DisplayContactModule import DisplayContactModule
from modules.submodules.UpdateWindow import UpdateWindow

class ListModule(Frame):

    def __init__(self, master=None, **kw):

        super().__init__(master=master, **kw)
        self.master = master
        self.db_path = path.join(path.dirname(__file__), pardir, 'contacts.db')

        self.style = Style()
        self.style.configure("Treeview.Heading", font="Helvetica 12")
        self.style.configure("Treeview.Column", font="Helvetica 12")

        self.searchField = Entry(master=self, font = "Helvetica 16", width=40)
        self.searchField.bind("<Return>", lambda e: self.runSearch())
        self.searchField.grid(row=0, column=0, columnspan=3, padx=1, pady=5, ipadx=2, ipady=2)

        self.searchButton = Button(master=self, fg="#ffffff", highlightbackground="#ffbb00", text='Search', width=8, command=self.runSearch)
        self.searchButton.grid(row=0, column=3, padx=10, pady=5, ipadx=4, ipady=4)

        self.insert_button = Button(master=self, fg="#ffffff", highlightbackground="#007d1d", text="Add", width=8, command=self.addContact)
        self.insert_button.grid(row=1, column=0, padx=10, pady=5, ipadx=4, ipady=4)

        self.delete_button = Button(master=self, fg="#ffffff", highlightbackground="#a3001b", text="Delete", width=8, command=self.deleteContact)
        self.delete_button.grid(row=1, column=1, padx=10, pady=5, ipadx=4, ipady=4)

        self.display_button = Button(master=self, fg="#ffffff", highlightbackground="#2b00ba", text="Display", width=8, command=self.displayContact)
        self.display_button.grid(row=1, column=2, padx=10, pady=5, ipadx=4, ipady=4)

        self.update_button = Button(master=self, fg="#ffffff", highlightbackground="#005ea6", text="Update", width=8, command=self.updateData)
        self.update_button.grid(row=1, column=3, padx=10, pady=5, ipadx=4, ipady=4)

        self.list = Treeview(master=self, columns=('Name'))
        self.list.grid(row=2, columnspan=4, padx=10, pady=10)

        self.verscrlbar = Scrollbar(master=self, orient='vertical', command=self.list.yview)
        self.verscrlbar.grid(row=2, column=4)

        self.list.configure(yscrollcommand = self.verscrlbar.set)

        self.list.heading('#0', text='ID')
        self.list.heading('#1', text='Name')

        self.list.column("#0", minwidth=30, width=40, stretch=False, anchor=CENTER)
        self.list.column("#1", minwidth=300, width=500, stretch=False, anchor=CENTER)

        self.populateList()

    def populateList(self):

        try:
            with connect(self.db_path) as conn:
                cursor = conn.cursor()
                contacts = cursor.execute("SELECT * FROM contacts").fetchall()
                self.list.delete(*self.list.get_children())
                for contact in contacts:
                    self.list.insert('', 'end', text=contact[0], values=(contact[1]))
        except:
            print('ERROR connecting to database!!!')

    def updateData(self):

        to_update = self.list.item(self.list.focus())['values'][0]

        root = Tk()
        frame = UpdateWindow(master=root, dbPath=self.db_path, cName=to_update)
        root.wait_window()
        self.populateList()

    def addContact(self):

        root = Tk()
        frame = NewContactModule(master=root)
        root.wait_window()
        self.populateList()

    def deleteContact(self):

        delete_name = self.list.item(self.list.focus())['values'][0]

        try:
            with connect(self.db_path) as conn:
                cursor = conn.cursor()
                query = f"DELETE FROM contacts WHERE name LIKE '%{str(delete_name)}%'"
                cursor.execute(query)
                conn.commit()
        except:
            print('Error occured somewhere')
        finally:
            self.populateList()

    def displayContact(self):

        display_contact = self.list.item(self.list.focus())['values'][0]

        root = Tk()
        frame = DisplayContactModule(master=root, info=display_contact)
        root.mainloop()

    def runSearch(self):

        search_query = self.searchField.get()
        self.searchField.delete(0, 'end')

        if(len(search_query) == 0):
            self.populateList()

        else:

            try:
                with connect(self.db_path) as conn:
                    query = f"SELECT * from contacts WHERE name LIKE '%{search_query}%'"
                    cursor = conn.cursor()
                    response = cursor.execute(query).fetchall()
                    self.list.delete(*self.list.get_children())
                    for contact in response:
                        self.list.insert('', 'end', text=contact[0], values=(contact[1]))
            except:
                print('Search failed')