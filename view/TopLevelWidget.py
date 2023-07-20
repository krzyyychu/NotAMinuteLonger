import tkinter

from tkinter import Frame, Button, Tk

from view.StopwatchWidget import StopwatchWidget
from view.SummaryWidget import SummaryWidget


class TopLevelWidget(Frame):
    """top level frame containing stopwatches, add/remove buttons and summary"""
    def __init__(self, tk_parent, controller, stopwatch_count=5, add_stopwatch_callback=None, *args, **kwargs):
        Frame.__init__(self, tk_parent, *args, **kwargs)
        self.parent = tkinter.Frame(tk_parent, **kwargs)
        self._controller = controller

        # create list of stopwatch views
        self.num_of_stopwatches = stopwatch_count
        self.widget_list = []
        self._add_stopwatch_callback = add_stopwatch_callback

        self.draw()

    def draw(self):
        self._add_stopwatches()
        self._add_button()
        self._add_summary()

        for w in self.widget_list:
            w.pack(fill="x")
        self.parent.pack()

    def set_stopwatch_time(self, stopwatch_id, value):
        self.widget_list[stopwatch_id].set_time(value)

    def set_stopwatch_description(self, stopwatch_id, value):
        self.widget_list[stopwatch_id].set_task_description(value)

    def set_summary(self, value):
        self.widget_list[-1].set_time(value)

    def _add_stopwatches(self):
        for stopwatch_id in range(self.num_of_stopwatches):
            self._create_stopwatch(stopwatch_id)

    def _create_stopwatch(self, stopwatch_id):
        stopwatch = StopwatchWidget(
            tk_parent=self.parent,
            stopwatch_id=stopwatch_id,
            start_button_callback=self._controller.notice_start,
            stop_button_callback=self._controller.notice_stop,
            entry_update_callback=self._controller.notice_entry_update)
        self.widget_list.append(stopwatch)

    def _add_button(self):
        self.widget_list.append(
            Button(
                self.parent,
                text="+",
                command=self._add_stopwatch_clicked))

    def _add_summary(self):
        self.widget_list.append(
            SummaryWidget(self.parent))

    def _add_stopwatch_clicked(self):
        self.num_of_stopwatches += 1
        for w in self.widget_list:
            w.destroy()
        self.widget_list.clear()
        self.draw()
        self._add_stopwatch_callback()



class ActivityManagerMock:
    def __init__(self):
        pass

    def notice_start(self, *args, **kwargs):
        pass

    def notice_stop(self, *args, **kwargs):
        pass

    def notice_entry_update(self, *args, **kwargs):
        pass

    def add_clicked(*args, **kwargs):
        pass


if __name__ == "__main__":
    root = tkinter.Tk()
    am = ActivityManagerMock
    widget = TopLevelWidget(root, am, 5)
    widget.pack()
    root.mainloop()
