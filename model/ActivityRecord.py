class ActivityRecord:
    def __init__(self, stopwatch_id, jira_id="", description="", time=0):
        self._stopwatch_id = stopwatch_id
        self._jira_id = jira_id
        self._description = description
        self._time = time

    def __repr__(self):
        return f"<model.StopwatchData> {self.stopwatch_id=}, {self.jira_id=}, {self.description=}, {self.time=}"

    @property
    def stopwatch_id(self):
        return self._stopwatch_id

    @stopwatch_id.setter
    def stopwatch_id(self, value):
        if value is None or value < 0:
            raise ValueError(f"stopwatch_id incorrect! {value=}")
        self._stopwatch_id = value

    @property
    def jira_id(self):
        return self._jira_id

    @jira_id.setter
    def jira_id(self, value):
        if value is None:
            self._jira_id = ""
        self._jira_id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None:
            self._description = ""
        self._description = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value < 0:
            raise ValueError(f"time cannot be negative! {self.stopwatch_id=}, {value=}")
        self._time = value