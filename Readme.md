# Simple phonebook app

## A simple phonebook app made with tkinter-sqlite.

**WARNING:** The database file must be present in the main directory, moving it to some other directory will cause the program to malfunction.

### Features

* The program auto-generates a database file on first instance of execution.
* Scrollbar stays inactive until the list overflows the viewpane
* A blank search would refresh the list and display all contacts
* Each insert or update function refreshes the list too

The entry point of the program is through `main.py`. Through there, the code has been distributed into separate files according to their functionalities. E.g. `NewContactModule.py` is used to insert new contacts into the phonebook. The code has been designed keeping in mind to refresh the list after any modifications whatsoever.

#### Exceptions

The background color of button widgets might behave inappropriately since winfo rgb does not work properly on the mac colors, this makes it difficult to get the proper default color. This issue originates in tcl upon which tkinter is built onto.
