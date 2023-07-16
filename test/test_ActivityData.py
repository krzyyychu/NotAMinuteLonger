import unittest

from model.ActivityData import ActivityData


class ActivityDataTest(unittest.TestCase):

    def test_updating_time(self):
        uut = ActivityData()
        uut.add_time(0, 3)
        uut.add_time(1, 42)
        uut.add_time(0, 123)
        self.assertEqual(uut.get_time(0), 126)
        self.assertEqual(uut.get_time(1), 42)
        self.assertEqual(uut.get_description(0), "")

    def test_updating_description(self):
        uut = ActivityData()
        uut.update_description(0, "a")
        uut.update_description(1, "cucumber")
        uut.update_description(0, "babbage")
        self.assertEqual(uut.get_description(0), "babbage")
        self.assertEqual(uut.get_description(1), "cucumber")
        self.assertEqual(uut.get_time(0), 0)

    def test_get_description_out_of_range_should_raise_IndexError(self):
        uut = ActivityData()
        self.assertRaises(IndexError, uut.get_description, 2)

    def test_get_time_out_of_range_should_raise_IndexError(self):
        uut = ActivityData()
        self.assertRaises(IndexError, uut.get_time, 2)

    def test_summary_retrieving(self):
        uut = ActivityData()
        uut.add_time(0, 3)
        uut.add_time(1, 42)
        uut.add_time(0, 123)
        self.assertEqual(uut.get_time_summary(), 168)
        self.assertEqual(uut.get_description(0), "")

    def test_add_stopwatches_from_list(self):
        expected = ActivityData()
        expected.add_time(0, 1)
        expected.update_description(0, "Alice")
        expected.add_time(1, 2)
        expected.update_description(1, "babbage")

        uut = ActivityData()
        uut.add_stopwatches_from_json_list([{"Alice": 1}, {"babbage": 2}])
        self.assertEqual(uut.get_time(0), expected.get_time(0))
        self.assertEqual(uut.get_time(1), expected.get_time(1))
        self.assertEqual(uut.get_description(0), expected.get_description(0))
        self.assertEqual(uut.get_description(1), expected.get_description(1))


if __name__ == '__main__':
    unittest.main()
