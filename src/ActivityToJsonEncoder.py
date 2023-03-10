import json
import tkinter #TODO remove after refactoring TkActivityManager
from json import JSONEncoder
from TkActivityManagerWidget import TkActivityManagerWidget
from TkStopwatchWidget import TkStopwatchWidget

class ActivityToJsonEncoder(JSONEncoder):
    def default(self, ob):
        if isinstance(ob, TkActivityManagerWidget):
            return {"stopwatches": ob.stopwatches}
        if isinstance(ob, TkStopwatchWidget):
            return {"time": ob.get_time_string().__str__()}
        else:
            return json.JSONEncoder.default(self, ob)




if __name__ == "__main__":
    root = tkinter.Tk()
    tam = TkActivityManagerWidget(root)

    print(ActivityToJsonEncoder().encode(tam))
