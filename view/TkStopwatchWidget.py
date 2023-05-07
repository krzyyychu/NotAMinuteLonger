import tkinter


class TkStopwatchWidget(tkinter.Frame):
    """Simple stopwatch widget"""

    def __init__(
            self,
            tk_parent: tkinter.Frame,
            stopwatch_id: int,
            elapsed_time=None,
            **kw):

        tkinter.Frame.__init__(self, tk_parent, kw)
        self._stopwatch_id = stopwatch_id

        self._taskname_entry = tkinter.Entry(self, width=24)
        self._taskname_entry.pack(side=tkinter.LEFT)

        self._time_string = tkinter.StringVar(self, "00:00:00")
        self._duration_label = tkinter.Label(self, textvariable=self._time_string)
        self._duration_label.pack(side=tkinter.LEFT)

        self._start_button = tkinter.Button(self, text="Start", command=self.start_clicked)
        self._start_button.pack(side=tkinter.LEFT)
        self._stop_button = tkinter.Button(self, text="Stop", command=self.stop_clicked)
        self._stop_button.pack(side=tkinter.LEFT)
        self._start_action = None
        self._stop_action = None

        self.update_time_label(elapsed_time)

    def update_time_label(self, elapsed: str):
        """ Set the time string to Hours:Minutes:Seconds"""
        elapsed = str(elapsed or '00:00:00')
        self._time_string.set(elapsed)

    def set_start_action(self, start_action):
        self._start_action = start_action

    def set_stop_action(self, stop_action):
        self._stop_action = stop_action

    def start_clicked(self):
        if self._start_action:
            self._start_action(self._stopwatch_id)

    def stop_clicked(self):
        if self._stop_action:
            self._stop_action(self._stopwatch_id)

    def get_id(self):
        return self._stopwatch_id


def demo():
    root = tkinter.Tk()
    widget = TkStopwatchWidget(root, None)
    widget.pack()
    root.mainloop()


if __name__ == "__main__":
    demo()

