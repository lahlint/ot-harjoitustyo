from tkinter import Tk, ttk, constants


class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Kirjautuminen")
        username_label = ttk.Label(master=self._root, text="Käyttäjänimi")
        username_entry = ttk.Entry(master=self._root)
        password_label = ttk.Label(master=self._root, text="Salasana")
        password_entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Kirjaudu")

        heading_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        button.grid(row=3, column=0, columnspan=2)


window = Tk()
window.title("Tasohyppelypeli")

ui = UI(window)
ui.start()


window.mainloop()
