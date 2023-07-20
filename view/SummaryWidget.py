import tkinter


class SummaryWidget(tkinter.Frame):
    def __init__(self, parent: tkinter.Frame, **kw):
        tkinter.Frame.__init__(self, parent, kw)
        self.parent = parent
        self.tk_summary_description = tkinter.Label(self, text="Total time:")
        self.tk_summary_description.pack(side=tkinter.LEFT)

        self._time_string = tkinter.StringVar(self, "00:00:00")
        self.tk_total_time = tkinter.Label(self, textvariable=self._time_string)
        self.tk_total_time.pack(side=tkinter.RIGHT)

    def set_time(self, time_sum: str) -> None:
        self._time_string.set(time_sum)
