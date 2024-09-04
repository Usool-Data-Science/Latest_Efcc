import os
import pep8
import unittest as ut
from models import app
from models import db
from models import bcrypt
import models.staff as stf
from models.staff import Staff
from models.petition import Petition
from datetime import datetime


os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
password = '123456'
pasw_hs = bcrypt.generate_password_hash(password).decode('utf-8')
staff1 = Staff(first_name="New", last_name="Staff",
               email="newadeshinaibrahim10@gmail.com",
               password=pasw_hs, age=30, gender="Male",
               state="Lagos", admin=True
               )


class TestStaff(ut.TestCase):
    """
    A blueprint for testing the staff object.
    1. Checks pep8 conformance for the module and its test file.
    2. Checks module and object level docstring.
    """
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_pep8_conformance_staff(self):
        """Checks if the staff module conforms with pep8 guide"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/staff.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning)")

    def test_pep8_conformance_test_staff(self):
        """Checks if the staff test module conforms with pep8 guide"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['test_staffs.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning)")

    def test_staff_module_doctstring(self):
        """Checks staff.py docstring"""
        self.assertIsNot(stf.__doc__, None,
                         "staff.py needs docstring")
        self.assertTrue(len(stf.__doc__) >= 1,
                        "staff.py needs a good docstring")

    def test_staff_class_doctstring(self):
        """Checks Staff object docstring"""
        self.assertIsNot(staff1.__doc__, None,
                         "staff.py needs docstring")
        self.assertTrue(len(staff1.__doc__) >= 1,
                        "staff.py needs a good docstring")

    def test_staff(self):
        """
        - Checks all attribute of the staff object.
        - Checks the relationship between staff and petition
        """
        petition1 = Petition(casefile_no="CASE1", cr_no="CR1",
                             date_received=datetime.now(),
                             date_assigned=datetime.now(),
                             amount_involved=1000, status_signal='UI',
                             staff_id=staff1.id,
                             petition_source='Regular-Complain')
        staff1.petitions.extend([petition1])

        self.assertIsInstance(staff1.first_name, str,
                              "Staff first name must be a string")
        self.assertIsInstance(staff1.last_name, str,
                              "Staff last name must be a string")
        self.assertIsInstance(staff1.email, str,
                              "Staff email must be a string")
        self.assertIsInstance(staff1.age, int,
                              "Staff age must be an integer")
        self.assertIsInstance(staff1.admin, int,
                              "Staff age must be an integer")
        self.assertIsInstance(staff1.petitions, list,
                              "Staff petitions must be a list")
        self.assertIsInstance(staff1.petitions[0], Petition,
                              "Staff petition must be a Petition")


if __name__ == "__main__":
    ut.main(verbosity=2)
