import tkinter


class StopwatchWidget(tkinter.Frame):
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

    def set_time(self, elapsed_time):
        """ Set the time string to Hours:Minutes:Seconds"""
        elapsed_time = str(elapsed_time or '00:00:00')
        self._time_string.set(elapsed_time)

    def set_task_description(self, new_description):
        self._entry_stringvar.set(new_description)

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
    def stop_clicked(stopwatch_id):
        print(f"{stopwatch_id}: stop clicked!")

    def start_clicked(stopwatch_id):
        print(f"{stopwatch_id}: start clicked")

    def task_name_changed(stopwatch_id, text):
        print(f"{stopwatch_id}: entry changed, new value: {text}")

    root = tkinter.Tk()
    widget = StopwatchWidget(
        root,
        stopwatch_id=0,
        start_button_callback=start_clicked,
        stop_button_callback=stop_clicked,
        entry_update_callback=task_name_changed)
    widget.pack()
    root.mainloop()


if __name__ == "__main__":
    demo()

