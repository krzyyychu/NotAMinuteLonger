import unittest

from CallbackMock import CallbackMock
from view.StopwatchWidget import StopwatchWidget


class TkStopwatchWidgetTest(unittest.TestCase):

    def test_class_creation(self):
        uut = StopwatchWidget(None, 0)
        self.assertEqual(uut._time_string.get(), "00:00:00")

    def test_set_elapsed_time(self):
        uut = StopwatchWidget(None, 0)
        uut.set_time("00:00:42")
        self.assertEqual(uut._time_string.get(), "00:00:42")

    def test_set_task_description(self):
        uut = StopwatchWidget(None, 0)
        uut.set_task_description("dog cuddling")
        self.assertEqual(uut._entry_stringvar.get(), "dog cuddling")

    def test_start_button_action_calls_callback(self):
        mock = CallbackMock()
        uut = StopwatchWidget(None, 0, start_button_callback=mock.mocked_callback)
        uut.start_clicked()
        uut.stop_clicked()
        uut.entry_changed()
        self.assertEqual(mock.times_called, 1)

    def test_stop_button_action_calls_callback(self):
        mock = CallbackMock()
        uut = StopwatchWidget(None, 0, stop_button_callback=mock.mocked_callback)
        uut.start_clicked()
        uut.stop_clicked()
        uut.entry_changed()
        self.assertEqual(mock.times_called, 1)

    def test_entry_changed_action_calls_callback(self):
        mock = CallbackMock()
        uut = StopwatchWidget(None, 0, entry_update_callback=mock.mocked_callback)
        uut.start_clicked()
        uut.stop_clicked()
        uut.entry_changed()
        self.assertEqual(mock.times_called, 1)


if __name__ == '__main__':
    unittest.main()
