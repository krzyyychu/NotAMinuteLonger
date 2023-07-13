import unittest

from model.ActivityData import ActivityData


class ActivityDataTest(unittest.TestCase):

    def test_updating_time(self):
        uut = ActivityData(stopwatch_count=3)
        uut.add_time(0, 3)
        uut.add_time(1, 42)
        uut.add_time(0, 123)
        self.assertEqual(uut.get_time(0), 126)
        self.assertEqual(uut.get_time(1), 42)
        self.assertEqual(uut.get_time(2), 0)
        self.assertEqual(uut.get_description(0), "")

    def test_updating_description(self):
        uut = ActivityData(stopwatch_count=3)
        uut.update_description(0, "a")
        uut.update_description(1, "cucumber")
        uut.update_description(0, "babbage")
        self.assertEqual(uut.get_description(0), "babbage")
        self.assertEqual(uut.get_description(1), "cucumber")
        self.assertEqual(uut.get_description(2), "")
        self.assertEqual(uut.get_time(0), 0)

    def test_summary_retrieving(self):
        uut = ActivityData(stopwatch_count=3)
        uut.add_time(0, 3)
        uut.add_time(1, 42)
        uut.add_time(0, 123)
        self.assertEqual(uut.get_time_summary(), 168)
        self.assertEqual(uut.get_description(0), "")


if __name__ == '__main__':
    unittest.main()
