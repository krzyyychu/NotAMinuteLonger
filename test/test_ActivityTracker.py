import unittest

from time import sleep
from CallbackMock import CallbackMock
from controller.ActivityTracker import ActivityTracker


class ActivityTrackerTest(unittest.TestCase):

    def test_time_tracking_activation(self):
        mock = CallbackMock()
        uut = ActivityTracker(inactivity_period=1, tick_callback=mock.mocked_callback)
        uut.activate()
        sleep(1.1)
        self.assertEqual(mock.times_called, 1)

    def test_time_tracking_deactivation(self):
        mock = CallbackMock()
        uut = ActivityTracker(inactivity_period=1, tick_callback=mock.mocked_callback)
        uut.activate()
        uut.deactivate()
        sleep(1.1)
        self.assertEqual(mock.times_called, 0)


if __name__ == '__main__':
    unittest.main()
