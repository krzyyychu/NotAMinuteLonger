import tkinter
from src.Controller.ActivityTracker import ActivityTracker
from src.View.TkStopwatchWidget import TkStopwatchWidget
from src.View.TkSummaryWidget import TkSummaryWidget


class ActivityManager:
    """Root class for activity manager.

    Has:
    + tkinter.Frame
    + list of stopwatches
    + summary widget
    + activity tracker
    - settings object

    Does:
    manages stopwatch list so only 1 stopwatch runs in parallel
    """

    def __init__(self, tk_parent, num_of_stopwatches=5, inactivity_period=3, **kw):
        self.frame = tkinter.Frame(tk_parent, kw)
        self.num_of_stopwatches = num_of_stopwatches
        self.stopwatches = []
        for stopwatch_id in range(num_of_stopwatches):
            stopwatch = TkStopwatchWidget(tk_parent=self.frame, controller=self, stopwatch_id=stopwatch_id)
            self.stopwatches.append(stopwatch)
            stopwatch.pack()
        self.current_stopwatch_id = 0
        self.current_stopwatch_active = False

        self.summary = TkSummaryWidget(self.frame, self.stopwatches)
        self.summary.pack()

        self.frame.pack()
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
    am = ActivityManager(root)
    root.title("ActivityTracker")
    root.resizable(width="false", height="false")
    root.mainloop()



