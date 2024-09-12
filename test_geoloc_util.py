
import unittest
from geoloc_util import get_location_by_name, get_location_by_zip

class TestGeoLocUtil(unittest.TestCase):

    def test_get_location_by_name(self):
        """
        Test valid location name search
        """
        result = get_location_by_name("Madison", "WI")
        self.assertIsNotNone(result), f"Result was {result}"
        self.assertIn('latitude', result)
        self.assertIn('longitude', result)

    def test_get_location_by_zip(self):
        """
        Test valid zip search
        """
        result = get_location_by_zip("12345")
        self.assertIsNotNone(result), f"Result was {result}"
        self.assertIn('latitude', result)
        self.assertIn('longitude', result)

    def test_get_location_by_bad_name(self):
        """
        Test invalid name search
        """
        result = get_location_by_name("@#$@#$", "!@#!@#")
        assert result == 'Error fetching location for @#$@#$, !@#!@#: 0'


    def test_get_location_by_bad_zip(self):
        """
        Test invalid Zip search
        """
        result = get_location_by_zip("1")
        assert 'invalid zip code' == result, f"Result was {result}"
