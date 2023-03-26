import tkinter
import time


class TkStopwatchWidget(tkinter.Frame):
    """Simple stopwatch widget"""

    def __init__(self, tk_parent=None, controller=None,  stopwatch_id=0, **kw):
        tkinter.Frame.__init__(self, tk_parent, kw)
        self.parent = tk_parent
        self._controller = controller
        self._stopwatch_id = stopwatch_id
        self._start = 0.0
        self._elapsed_time = 0.0
        self._running = 0
        self._time_string = tkinter.StringVar(self, "00:00:00")

        self.task_name = tkinter.Entry(self, width=24)
        self.task_name.pack(side=tkinter.LEFT)

        duration_label = tkinter.Label(self, textvariable=self._time_string)
        self.__setTime(self._elapsed_time)
        duration_label.pack(side=tkinter.LEFT)

        play_button = tkinter.Button(self, text="Start", command=self.start_clicked)
        play_button.pack(side=tkinter.LEFT)
        stop_button = tkinter.Button(self, text="Stop", command=self.stop_clicked)
        stop_button.pack(side=tkinter.LEFT)

    def __setTime(self, elapsed):
        """ Set the time string to Hours:Minutes:Seconds"""
        hours = int(elapsed / 3600)
        minutes = int(elapsed / 60 - hours * 60.0)
        seconds = int(elapsed - minutes * 60.0)
        self._time_string.set('%02d:%02d:%02d' % (hours, minutes, seconds))

    def __update(self):
        """ Update the label with elapsed time. """
        self._elapsed_time = time.time() - self._start
        self.__setTime(self._elapsed_time)
        self._timer = self.after(1000, self.__update)

    def start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsed_time
            self.__update()
            self._running = True

    def stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsed_time = time.time() - self._start
            self.__setTime(self._elapsed_time)
            self._running = False

    def start_clicked(self):
        self.start()
        if self._controller:
            self._controller.notice_start(self._stopwatch_id)

    def stop_clicked(self):
        self.stop()
        if self._controller:
            self._controller.notice_stop(self._stopwatch_id)

    def get_id(self):
        return self._stopwatch_id

    def get_time(self):
        return self._elapsed_time

    def get_time_string(self):
        return self._time_string.get()

    def get_task_name(self):
        return self.task_name.get()


if __name__ == "__main__":
    root = tkinter.Tk()
    sw1 = TkStopwatchWidget(root)
    sw1.pack()
    sw2 = TkStopwatchWidget(root)
    sw2.pack()
    root.title("ActivityTracker")
    root.resizable(width="false", height="false")
    root.mainloop()