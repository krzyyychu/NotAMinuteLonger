import unittest

from model.ActivityDataEncoder import ActivityDataEncoder
from model.ActivityData import ActivityData


class ActivityDataEncoderTest(unittest.TestCase):

    def test_encoding_empty_ActivityData(self):
        data = ActivityData(stopwatch_count=0)
        output = ActivityDataEncoder().encode(data)
        self.assertEqual(
            output,
            '{"stopwatches": []}')

    def test_encoding_empty_stopwatches(self):
        data = ActivityData(stopwatch_count=2)
        output = ActivityDataEncoder().encode(data)
        self.assertEqual(
            output,
            '{"stopwatches": ['
                '{"task_0": 0}, '
                '{"task_1": 0}'
            ']}')

    def test_encoding(self):
        data = ActivityData(stopwatch_count=3)
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
