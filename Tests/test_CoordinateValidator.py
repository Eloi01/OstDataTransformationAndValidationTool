from unittest import TestCase

import CoordinateValidator


class Test(TestCase):

    def test_extract_geo_coordinate(self):
        test_string = "-12.9989"
        result_string = "-12.9989"
        self.assertEqual( result_string,CoordinateValidator.extract_geo_coordinates(test_string))

    def test_validate_longitude(self):
        test_string = "-12.1"
        result_string = True
        self.assertEqual(CoordinateValidator.validate_longitude(test_string), result_string)

    def test_validate_invalid_longitude(self):
        test_string = "-200"
        result_string = False
        self.assertEqual(CoordinateValidator.validate_longitude(test_string), result_string)

    def test_validate_latitude(self):
        test_string = "-179.11111"
        result_string = True
        self.assertEqual(CoordinateValidator.validate_latitude(test_string), result_string)

    def test_validate_invalid_latitude(self):
        test_string = "250"
        result_string = False
        self.assertEqual(CoordinateValidator.validate_latitude(test_string), result_string)

    def test_extract_geo_point(self):
        test_string = "250, 120.99903"
        result_string = ["250", "120.99903"]
        self.assertEqual(CoordinateValidator.extract_geo_point(test_string), result_string)

    def test_validate_geo_point(self):
        test_string = "250, 120.99903"
        result_string = True
        self.assertEqual(CoordinateValidator.validate_point(test_string), result_string)

    def test_validate_invalid_geo_point(self):
        test_string = "250, 120.99903, 99.11"
        result_string = False
        self.assertEqual(CoordinateValidator.validate_point(test_string), result_string)
