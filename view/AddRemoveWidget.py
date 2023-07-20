import tkinter


class AddRemoveWidget(tkinter.Frame):
    """widget containing add and remove buttons"""

    def __init__(
            self,
            tk_parent: tkinter.Frame,
            add_button_callback=None,
            remove_button_callback=None,
            **kw):

        tkinter.Frame.__init__(self, tk_parent, kw)
        self._entry = tkinter.Button(tk_parent, text="+", command=self.add_clicked)
        self._entry.pack(fill="x")

        # assign actions
        self._add_action = add_button_callback
        self._remove_action = remove_button_callback

    def add_clicked(self):
        if self._add_action:
            self._add_action()

    def remove_clicked(self):
        if self._remove_action:
            self._remove_action(self._remove_action)


def demo():
    def add_clicked():
        print("clicked!")
        pass

    def remove_clicked():
        pass

    root = tkinter.Tk()
    widget = AddRemoveWidget(
        root,
        add_button_callback=add_clicked,
        remove_button_callback=remove_clicked)
    widget.pack()
    root.mainloop()


if __name__ == "__main__":
    demo()

