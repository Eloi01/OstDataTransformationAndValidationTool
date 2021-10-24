from unittest import TestCase

import DateValidator


class Test(TestCase):
    def test_duration_date(self):
        test_string = "1999/2000"
        result_string = "1999/2000"
        self.assertEqual(DateValidator.check_date_duration_format(test_string), result_string)

    def test_duration2_date(self):
        test_string = "1999-01-01/2000-01-01"
        result_string = "1999-01-01/2000-01-01"
        self.assertEqual(DateValidator.check_date_duration_format(test_string), result_string)

    def test_wrong_duration_format_date(self):
        test_string = "1999-01-01-9999/2000-01-01"
        result_string = False
        self.assertEqual(DateValidator.check_date_duration_format(test_string), result_string)

    def test_date(self):
        test_string = "1999-01-01"
        result_string = "1999-01-01"
        self.assertEqual(DateValidator.extract_date_format(test_string), result_string)

    def test2_date(self):
        test_string = "1999-01"
        result_string = "1999-01"
        self.assertEqual(DateValidator.extract_date_format(test_string), result_string)

    def test_wrong_date_format(self):
        test_string = "1999-01-01-"
        result_string = False
        self.assertEqual(DateValidator.extract_date_format(test_string), result_string)



