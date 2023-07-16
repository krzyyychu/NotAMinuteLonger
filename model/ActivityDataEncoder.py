from json import JSONEncoder

from model.ActivityData import ActivityData, StopwatchData


class ActivityDataEncoder(JSONEncoder):
    """JSONEncoder specialized to encode stopwatch data"""
    def default(self, obj):
        if isinstance(obj, ActivityData):
            return {"stopwatches": obj.get_stopwatches()}
        if isinstance(obj, StopwatchData):
            task_name = obj.description
            task_name = task_name if task_name else "task_"+str(obj.id)
            return {task_name: obj.time}
        else:
            return JSONEncoder.default(self, obj)


if __name__ == "__main__":
    am = ActivityData()

    print(ActivityDataEncoder().encode(am))
