import unittest
from models.petition import Petition


class TestPetition(unittest.TestCase):
    """
    Petition test blueprint:
    """
    @classmethod
    def setUpClass(self):
        print("petition class setUp")
    
    @classmethod
    def tearDownClass(self):
        print("petition class teardown")


if __name__ == "__main__":
    unittest.main()