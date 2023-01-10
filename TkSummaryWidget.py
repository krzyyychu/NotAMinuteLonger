import tkinter
from threading import Thread
from time import sleep

from TkStopwatchWidget import TkStopwatchWidget


class TkSummaryWidget(tkinter.Frame):
    def __init__(self, parent=None, stopwatch_list=[], **kw):
        tkinter.Frame.__init__(self, parent, kw)
        self.parent = parent
        self.tk_summary_description = tkinter.Label(self, text="Total time:")
        self.tk_summary_description.pack(side=tkinter.LEFT)

        self._time_string = tkinter.StringVar()
        self.tk_total_time = tkinter.Label(self, textvariable=self._time_string)

        self.tk_total_time.pack(side=tkinter.RIGHT)
        self.stopwatch_list = stopwatch_list
        self.timer = Thread(target=self.sum_time, daemon=True)
        self.timer.start()

    def sum_time(self):
        while True:
            time = 0
            for s in self.stopwatch_list:
                time += s.get_time()
            self.__set_time(time)
            sleep(1)


    def __set_time(self, elapsed):
        """ Set the time string to Hours:Minutes:Seconds"""
        hours = int(elapsed / 3600)
        minutes = int(elapsed / 60 - hours * 60.0)
        seconds = int(elapsed - minutes * 60.0)
        self._time_string.set('%02d:%02d:%02d' % (hours, minutes, seconds))


class TkActivityManagerMock(tkinter.Frame):
    #for testing purposes
    def __init__(self, parent=None, **kw):
        tkinter.Frame.__init__(self, parent, kw)
        self.parent = parent

    def notice_start(self, stopwatch_id):
        pass

    def notice_stop(self, stopwatch_id):
        pass


if __name__ == "__main__":
    root = tkinter.Tk()
    tam_mock = TkActivityManagerMock(root)
    tam_mock.pack()
    stopwatches = [TkStopwatchWidget(tam_mock) for x in range(4)]
    for stopwatch in stopwatches:
        stopwatch.pack()
    tk_summary = TkSummaryWidget(root, stopwatches)
    tk_summary.pack()
    root.title("ActivityTracker")
    root.resizable(width="false", height="false")
    root.mainloop()
