
class Settings:
    def __init__(self, inactivity_period=3, tasklist_len=5, font_size = 12):
        self._inactivity_period = inactivity_period
        self._tasklist_len = tasklist_len
        self._font_size = font_size
        self._show_description = True
        self._show_dialogs = True
        self._stopwatches_limit = 20

    @property
    def inactivity_period(self):
        return self._inactivity_period

    @property
    def tasklist_len(self):
        return self._tasklist_len

    @property
    def font_size(self):
        return self._font_size

    @property
    def stopwatches_limit(self):
        return self._stopwatches_limit
