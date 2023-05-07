
class Settings:
    def __init__(self, inactivity_period=3, tasklist_len=5, font_size = 12):
        self._inactivity_period = inactivity_period
        self._tasklist_len = tasklist_len
        self._font_size = font_size

    @property
    def inactivity_period(self):
        return self._inactivity_period

    @property
    def tasklist_len(self):
        return self._tasklist_len

    @property
    def font_size(self):
        return self._font_size

