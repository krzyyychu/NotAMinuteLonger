import tkinter


class TkStopwatchWidget(tkinter.Frame):
    """Simple stopwatch widget"""

    def __init__(
            self,
            tk_parent: tkinter.Frame,
            stopwatch_id: int,
            start_button_callback=None,
            stop_button_callback=None,
            entry_update_callback=None,
            **kw):

        tkinter.Frame.__init__(self, tk_parent, kw)
        self._stopwatch_id = stopwatch_id

        self._entry_stringvar = tkinter.StringVar(self, "")
        self._entry = tkinter.Entry(self, textvariable=self._entry_stringvar, width=24)
        self._entry.pack(side=tkinter.LEFT)

        self._time_string = tkinter.StringVar(self, "00:00:00")
        self._duration_label = tkinter.Label(self, textvariable=self._time_string)
        self._duration_label.pack(side=tkinter.LEFT)

        self._start_button = tkinter.Button(self, text="Start", command=self.start_clicked)
        self._start_button.pack(side=tkinter.LEFT)
        self._stop_button = tkinter.Button(self, text="Stop", command=self.stop_clicked)
        self._stop_button.pack(side=tkinter.LEFT)

        # assign actions
        self._start_action = start_button_callback
        self._stop_action = stop_button_callback
        self._entry_update_action = entry_update_callback
        self._entry_stringvar.trace_add("write", self.entry_changed)

    def set_elapsed_time(self, elapsed_time):
        self.update_time_label(elapsed_time)

    def update_time_label(self, elapsed: str):
        """ Set the time string to Hours:Minutes:Seconds"""
        elapsed = str(elapsed or '00:00:00')
        self._time_string.set(elapsed)

    def start_clicked(self):
        if self._start_action:
            self._start_action(self._stopwatch_id)

    def stop_clicked(self):
        if self._stop_action:
            self._stop_action(self._stopwatch_id)

    def entry_changed(self, *args, **kwargs):

        if self._entry_update_action:
            self._entry_update_action(self._stopwatch_id, self._entry_stringvar.get())

    def get_id(self):
        return self._stopwatch_id


def demo():
    def stop_clicked(id):
        print(f"{id}: stop clicked!")

    def start_clicked(id):
        print(f"{id}: start clicked")

    def task_name_changed(id, text):
        print(f"{id}: entry changed, new value: {text}")

    root = tkinter.Tk()
    widget = TkStopwatchWidget(
        root,
        stopwatch_id=0,
        start_button_callback=start_clicked,
        stop_button_callback=stop_clicked,
        entry_update_callback=task_name_changed)
    widget.pack()
    root.mainloop()


if __name__ == "__main__":
    demo()

