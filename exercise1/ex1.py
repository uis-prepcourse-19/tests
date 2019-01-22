import unittest
from test.score import Score
from user.exercise1.exercise1 import falling_object, sum_integers, falling_object_more

class TestFallingObject(unittest.TestCase):
    score = Score(10, 10, 'TestFallingObject')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def test_normal_case_1(self):
        self.points_worth = 4
        self.assertEqual(falling_object(10), 981.00)

    def test_normal_case_2(self):
        self.points_worth = 4
        self.assertEqual(falling_object(56), 30764.16)

    def test_falling_object_negative(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object(-1)


class TestSumIntegers(unittest.TestCase):
    score = Score(8, 20, 'TestSumIntegers')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def test_normal_case_1(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([10, 10]), 20)

    def test_normal_case_2(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([90, 10, 45, 25]), 170)

    def test_zero(self):
        self.points_worth = 2
        self.assertEqual(sum_integers([0, 0]), 0)

    def test_negative(self):
        self.points_worth = 2
        with self.assertRaises(Exception): sum_integers([1, 20, -1])


class TestFallingObjectMore (unittest.TestCase):
    score = Score(10, 20, 'TestFallingObjectMore')
    points_worth = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.score.write_json())

    def tearDown(self):  # https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method : hynekcer
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = result.errors
        failure = result.failures
        ok = not error and not failure
        if ok:
            self.score.increment_by(self.points_worth)

    def test_normal_case_1(self):
        self.points_worth = 2
        self.assertEqual(falling_object_more(20, 5), [3924.00, 15696.00, 15696.00, 35316.00, 62784.00])

    def test_zero_1(self):
        self.points_worth = 2
        self.assertEqual(falling_object_more(3, 0), [])

    def test_zero_2(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object_more(0, 3)

    def test_negative_1(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object_more(-1, 3)

    def test_negative_2(self):
        self.points_worth = 2
        with self.assertRaises(Exception): falling_object_more(1, -1)
