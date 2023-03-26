from json import JSONEncoder
from Controller.ActivityManager import ActivityManager
from View.TkStopwatchWidget import TkStopwatchWidget

from tkinter import Tk #TODO: probably can be replaced by some mock


class ActivityToJsonEncoder(JSONEncoder):
    """JSONEncoder specialized to encode stopwatch data"""
    def default(self, ob):
        if isinstance(ob, ActivityManager):
            return {"stopwatches": ob.stopwatches}
        if isinstance(ob, TkStopwatchWidget):
            task_name = ob.get_task_name().__str__()
            task_name = task_name if task_name else "task_"+str(ob.get_id())
            return {task_name: ob.get_time_string().__str__()}
        else:
            return json.JSONEncoder.default(self, ob)




if __name__ == "__main__":
    root = Tk()
    am = ActivityManager(root)

    print(ActivityToJsonEncoder().encode(am))
