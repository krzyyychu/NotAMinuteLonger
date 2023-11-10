
class Settings:
    def __init__(self,
                 inactivity_period=3,
                 tasklist_len=5,
                 font_size=12,
                 show_field_headers=True,
                 show_description_field=True,
                 show_jira_id_field=True,
                 show_dialogs=True,
                 stopwatches_max=30):
        self._inactivity_period = inactivity_period
        self._tasklist_len = tasklist_len
        self._font_size = font_size
        self._show_field_headers = show_field_headers
        self._show_description_field = show_description_field
        self._show_jira_id_field = show_jira_id_field
        self._show_dialogs = show_dialogs
        self._stopwatches_max = stopwatches_max

    @property
    def inactivity_period(self):
        return self._inactivity_period

    @inactivity_period.setter
    def inactivity_period(self, value: int):
        if value is None or value < 1:
            raise ValueError(f"tracked inactivity period cannot be less than one: {value=}")
        self._inactivity_period = value

    @property
    def tasklist_len(self):
        return self._tasklist_len

    @tasklist_len.setter
    def tasklist_len(self, value: int):
        if value is None or value < 0:
            raise ValueError(f"length of tasklist cannot be less than zero: {value=}")
        self._tasklist_len = value

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value: int):
        if value is None or value < 6:
            raise ValueError(f"font_size cannot be less than six: {value=}")
        self._font_size = value

    @property
    def stopwatches_limit(self):
        """There is no setter, please keep it this way."""
        return self._stopwatches_max
