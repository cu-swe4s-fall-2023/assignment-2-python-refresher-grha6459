import unittest
# duplicate import, not sure of best practices here
import numpy as np
import sys
sys.path.append('../../src')

import my_utils  # noqa
# Make test arrays
test_arr_rand = np.random.rand(5)
test_arr_contains_NaN = np.array([5, 5, 7, np.NAN])
test_arr_empty = np.array([])


class TestStats(unittest.TestCase):
    def test_mean(self):
        # Positive test case
        self.assertEqual(my_utils.get_mean(test_arr_rand),
                         np.sum(test_arr_rand) / np.shape(test_arr_rand)[0])
        # Negative test case, if the array is empty, this is not the same as a
        # mean of zero!
        self.assertIs(my_utils.get_mean(test_arr_empty), None)
        # Second Negative test case, if there are missing values, function
        # returns none
        self.assertIs(my_utils.get_mean(test_arr_contains_NaN), None)

    def test_median(self):
        # Positive test case
        self.assertEqual(my_utils.get_median(test_arr_rand),
                         np.median(test_arr_rand))
        # Negative test case, if the array is empty, this is not the same as a
        # median of zero!
        self.assertIs(my_utils.get_median(test_arr_empty), None)
        # Second Negative test case, if there are missing values, function
        # returns none
        self.assertIs(my_utils.get_median(test_arr_contains_NaN), None)

    def test_std(self):
        # Positive test case
        self.assertEqual(my_utils.get_median(test_arr_rand),
                         np.median(test_arr_rand))
        # Negative test case, if the array is empty, this is not the same as a
        # standard deviation of zero!
        self.assertIs(my_utils.get_median(test_arr_empty), None)
        # Second Negative test case, if there are missing values, function
        # returns none
        self.assertIs(my_utils.get_median(test_arr_contains_NaN), None)


if __name__ == '__main__':
    unittest.main()
