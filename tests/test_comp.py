import unittest
# from tests import test_pet
# from tests.test_pet import TestPetition
from models.complainant import Complainant


class TestComplainant(unittest.TestCase):
    """
    The following test cases are being handled:
    1. All attributes are correctly assigned
    """
    def setUp(self):
        """Instantiate the complainant object"""
        self.complainant1 = Complainant(name="testing",petition_ids=[], suspect_ids=[])
    
    def tearDown(self):
        """Clear of the attribute space"""
        del self.complainant1
    
    def test_attribute_present(self):
        """Tests if the complainants attributes are present"""
        self.assertTrue("name" in self.complainant1.__dict__)
        self.assertTrue("petition_ids" in self.complainant1.__dict__)
        self.assertTrue("suspect_ids" in self.complainant1.__dict__)


    def test_correct_assignment(self):
        self.assertEqual(self.complainant1.name, "testing")
        self.assertEqual(self.complainant1.petition_ids, [])
        self.assertEqual(self.complainant1.suspect_ids, [])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCases(TestComplainant)
    unittest.TextTestRunner(verbosity=2).run(suite)