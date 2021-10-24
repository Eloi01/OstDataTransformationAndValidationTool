from unittest import TestCase

import LODValidator


class Test(TestCase):
    def test_extract_gnd_link(self):
        test_string = r"http://d-nb.info/gnd/1234567"
        result_string = ["http://d-nb.info/gnd/1234567"]
        self.assertEqual(LODValidator.extract_gnd_link(test_string), result_string)

    def test_extract_gnd2_link(self):
        test_string = r"http://d-nb.info/gnd/1234567-1"
        result_string = ["http://d-nb.info/gnd/1234567-1"]
        self.assertEqual(LODValidator.extract_gnd_link(test_string), result_string)

    def test_extract_viaf_link(self):
        test_string = r"http://viaf.org/viaf/12345678"
        result_string = ["http://viaf.org/viaf/12345678"]
        self.assertEqual(LODValidator.extract_viaf_link(test_string), result_string)

    def test_extract_orcid_link(self):
        test_string = r"https://orcid.org/1234-1234-1234-123X"
        result_string = ["https://orcid.org/1234-1234-1234-123X"]
        self.assertEqual(LODValidator.extract_orcid_link(test_string), result_string)

    def test_extract_ror_link(self):
        test_string = r"https://ror.org/0567olm22"
        result_string = ["https://ror.org/0567olm22"]
        self.assertEqual(LODValidator.extract_ror_link(test_string), result_string)

    def test_extract_invalid_ror_link(self):
        test_string = r"https://ror.org/05L7olm22"
        result_string = []
        self.assertEqual(LODValidator.extract_ror_link(test_string), result_string)
