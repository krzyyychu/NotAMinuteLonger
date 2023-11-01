import unittest

from model.ActivityDataEncoder import ActivityDataEncoder
from model.Activities import Activities
from model.Settings import Settings


class ActivityDataEncoderTest(unittest.TestCase):
    def test_encoding_empty_ActivityData(self):
        data = Activities(settings=Settings())
        output = ActivityDataEncoder().encode(data)
        self.assertEqual(
            output,
            '{"stopwatches": []}')

    def test_encoding_stopwatches_without_description(self):
        data = Activities(settings=Settings())
        data.add_time(stopwatch_id=0, value=0)
        data.add_time(stopwatch_id=1, value=1)
        output = ActivityDataEncoder().encode(data)
        self.assertEqual(
            output,
            '{"stopwatches": ['
            '{"task_0": 0}, '
            '{"task_1": 1}'
            ']}')

    def test_encoding(self):
        data = Activities(settings=Settings())
        data.update_description(0, "fooling around")
        data.update_description(1, "dog walking")
        data.update_description(2, "dog cuddling")
        data.add_time(0, 3)
        data.add_time(1, 42)
        data.add_time(2, 123)
        output = ActivityDataEncoder().encode(data)
        self.assertEqual(
            output,
            '{"stopwatches": ['
            '{"fooling around": 3}, '
            '{"dog walking": 42}, '
            '{"dog cuddling": 123}'
            ']}')


if __name__ == '__main__':
    unittest.main()
