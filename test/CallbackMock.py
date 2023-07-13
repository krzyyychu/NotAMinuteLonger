
class CallbackMock:
    def __init__(self):
        self.times_called = 0

    def mocked_callback(self, *args):
        self.times_called += 1
