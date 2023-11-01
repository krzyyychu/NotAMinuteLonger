from json import JSONEncoder

from model.Activities import Activities, ActivityRecord


class ActivityDataEncoder(JSONEncoder):
    """JSONEncoder specialized to encode stopwatch data"""
    def default(self, obj):
        if isinstance(obj, Activities):
            return {"stopwatches": obj.get_stopwatches()}
        if isinstance(obj, ActivityRecord):
            task_name = obj.description
            task_name = task_name if task_name else "task_"+str(obj.stopwatch_id)
            return {task_name: obj.time}
        else:
            return JSONEncoder.default(self, obj)


if __name__ == "__main__":
    am = Activities()

    print(ActivityDataEncoder().encode(am))
