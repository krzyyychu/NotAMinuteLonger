import unittest

from view.TkStopwatchWidget import TkStopwatchWidget


class TkStopwatchWidgetTest(unittest.TestCase):

    def test_class_creation(self):
        uut = TkStopwatchWidget(None, 0)
        self.assertEqual(uut._time_string.get(), "00:00:00")

    def test_set_elapsed_time(self):
        uut = TkStopwatchWidget(None, 0)
        uut.set_elapsed_time("00:00:42")
        self.assertEqual(uut._time_string.get(), "00:00:42")


if __name__ == '__main__':
    unittest.main()
