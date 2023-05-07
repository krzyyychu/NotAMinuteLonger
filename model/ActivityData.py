

class StopwatchData:
    def __init__(self):
        self.description = ""
        self.time = 0

    #TODO: should be proper properties


class ActivityData:
    # Should this be POD?
    def __init__(self, stopwatch_count):
        self._stopwatch_count = stopwatch_count
        self._stopwatch_data = []
        for stopwatch_id in range(stopwatch_count):
            self._stopwatch_data.append(StopwatchData())

    def update_time(self, stopwatch_id, value):
        if 0 <= stopwatch_id < self._stopwatch_count:
            self._stopwatch_data[stopwatch_id].time += value

    def get_time(self, stopwatch_id):
        if 0 <= stopwatch_id < self._stopwatch_count:
            return self._stopwatch_data[stopwatch_id].time

    def get_time_summary(self):
        return sum([stopwatch.time for stopwatch in self._stopwatch_data])

    def update_description(self, stopwatch_id, label_text):
        if 0 <= stopwatch_id < self._stopwatch_count:
            self._stopwatch_data[stopwatch_id].description = label_text

    def get_description(self, stopwatch_id):
        if 0 <= stopwatch_id < self._stopwatch_count:
            return self._stopwatch_data[stopwatch_id].description

