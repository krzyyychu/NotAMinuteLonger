import tkinter
import time

from controller.ActivityTracker import ActivityTracker
from view.TkStopwatchWidget import TkStopwatchWidget
from view.TkSummaryWidget import TkSummaryWidget
from model.ActivityData import ActivityData


class ActivityManager:
    """Root class for activity manager.

    Has:
    + it's main tkinter.Frame
    + list of stopwatches
    + summary widget
    + activity tracker
    + activityData structure
    - settings object

    Does:
    manages stopwatch list so only 1 stopwatch runs in parallel
    """

    def __init__(self, tk_parent, stopwatch_count=5, inactivity_period=3, **kw):
        self.frame = tkinter.Frame(tk_parent, kw)

        # create list of stopwatch views
        self.num_of_stopwatches = stopwatch_count
        self.stopwatches = []
        for stopwatch_id in range(stopwatch_count):
            stopwatch = TkStopwatchWidget(tk_parent=self.frame, stopwatch_id=stopwatch_id)
            stopwatch.set_start_action(self.notice_start)
            stopwatch.set_stop_action(self.notice_stop)
            self.stopwatches.append(stopwatch)
            stopwatch.pack()
        self.summary = TkSummaryWidget(self.frame)
        self.summary.pack()

        # create corresponding models
        self.activity_data = ActivityData(stopwatch_count)

        # perform rest of initialization
        self.current_stopwatch_id = 0
        self.current_stopwatch_active = False

        self.frame.pack()
        self.activity_tracker = ActivityTracker(inactivity_period, self.on_active_tick)

    def on_active_tick(self):
        print("tick!")
        self.update_data()
        self.update_widgets()

    def update_data(self):
        self.activity_data.update_time(self.current_stopwatch_id, 1)

    def update_widgets(self):
        time_str = time.strftime("%H:%M:%S", time.gmtime(self.activity_data.get_time(self.current_stopwatch_id)))
        self.stopwatches[self.current_stopwatch_id].update_time_label(time_str)

        time_summary_str = time.strftime("%H:%M:%S", time.gmtime(self.activity_data.get_time_summary()))
        self.summary.update_time_label(time_summary_str)

    def notice_start(self, stopwatch_id):
        print(f"widget: {stopwatch_id=} start button clicked")
        self.current_stopwatch_id = stopwatch_id
        self.activity_tracker.activate()

    def notice_stop(self, stopwatch_id):
        print(f"widget: {stopwatch_id=} stop button clicked")
        if self.current_stopwatch_id == stopwatch_id:
            self.activity_tracker.deactivate()


if __name__ == "__main__":
    root = tkinter.Tk()
    am = ActivityManager(root)
    root.title("ActivityTracker")
    root.resizable(width="false", height="false")
    root.mainloop()



