import tkinter
from ActivityTracker import ActivityTracker
from TkStopwatchWidget import TkStopwatchWidget


class TkActivityManagerWidget(tkinter.Frame):
    def __init__(self, parent=None, num_of_stopwatches=5, inactivity_period=3, **kw):
        tkinter.Frame.__init__(self, parent, kw)
        self.num_of_stopwatches = num_of_stopwatches
        self.stopwatches = []
        for stopwatch_id in range(num_of_stopwatches):
            stopwatch = TkStopwatchWidget(self, stopwatch_id)
            self.stopwatches.append(stopwatch)
            stopwatch.pack()
        self.current_stopwatch_id = 0
        self.current_stopwatch_active = False
        #duration_label = tkinter.Label(self, textvariable="QPA")
        #duration_label.pack()
        self.activity_tracker = ActivityTracker(inactivity_period, self.on_activity, self.on_inactivity)

    def on_inactivity(self):
        print("Inactive!")
        if self.current_stopwatch_active:
            self.stopwatches[self.current_stopwatch_id].stop()

    def on_activity(self):
        print("Active!")
        if self.current_stopwatch_active:
            self.stopwatches[self.current_stopwatch_id].start()

    def notice_start(self, stopwatch_id):
        print(f"children button clicked: {stopwatch_id=}")
        self.current_stopwatch_id = stopwatch_id
        self.current_stopwatch_active = True
        for stopwatch in self.stopwatches:
            if stopwatch.get_id() != self.current_stopwatch_id:
                stopwatch.stop()

    def notice_stop(self, stopwatch_id):
        print(f"children button stop clicked: {stopwatch_id=}")
        self.current_stopwatch_active = False


if __name__ == "__main__":
    root = tkinter.Tk()
    tam = TkActivityManagerWidget(root)
    tam.pack()
    root.title("ActivityTracker")
    root.resizable(width="false", height="false")
    root.mainloop()



