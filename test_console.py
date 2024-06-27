#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup.

        Temporarily rename any existing databases/file.json.
        Reset FileStorage objects dictionary.
        Create an instance of the command interpreter.
        """
        try:
            os.rename("databases/file.json", "tmp")
        except IOError:
            pass
        # Create an instance of the HBNBCommand class. This allows the test
        # methods within the class to access and use this instance during the
        # testing process.
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown.

        Restore original databases/file.json.
        Delete the test HBNBCommand instance.
        """
        try:
            os.rename("tmp", "databases/file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created databases/file.json."""
        try:
            os.remove("databases/file.json")
        except IOError:
            pass

    def test_create_for_errors(self):
        """Test create command errors."""
        # Test if class name is missing
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        # Test if class doesn't exist
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
        """Test create command."""
        # Create BaseModel instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bmd = f.getvalue().strip()

        # Create FingerPrint instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create FingerPrint")
            fpt = f.getvalue().strip()

        # Create Petition instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Petition")
            ptn = f.getvalue().strip()

        # Create Suspect instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Suspect")
            spt = f.getvalue().strip()

        # Create Complainant instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Complainant")
            cpt = f.getvalue().strip()

        # Create Identity instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Identity")
            idt = f.getvalue().strip()

        # Create Recovery instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Recovery")
            rcv = f.getvalue().strip()
        # Create Monetary instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Monetary")
            mny = f.getvalue().strip()
        # Create Bank instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Bank")
            bnk = f.getvalue().strip()
        # Create Crypto instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Crypto")
            cry = f.getvalue().strip()
        # Create Cash instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Cash")
            csh = f.getvalue().strip()
        # Create Automobile instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Automobile")
            atm = f.getvalue().strip()
        # Create Electronic instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Electronic")
            elc = f.getvalue().strip()
        # Create Phone instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Phone")
            phn = f.getvalue().strip()
        # Create Laptop instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Laptop")
            lpt = f.getvalue().strip()
        # Create Other instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Other")
            oth = f.getvalue().strip()
        # Create Jewelry instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Jewelry")
            jwy = f.getvalue().strip()
        # Create LanddedProperty instance and capture its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create LandedProperty")
            lnd = f.getvalue().strip()

        
        # Test if the created instances are in the output of "all" command
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bmd, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all FingerPrint")
            self.assertIn(fpt, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Petition")
            self.assertIn(ptn, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Suspect")
            self.assertIn(spt, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Complainant")
            self.assertIn(cpt, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Identity")
            self.assertIn(idt, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Recovery")
            self.assertIn(rcv, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Monetary")
            self.assertIn(mny, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Bank")
            self.assertIn(bnk, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Crypto")
            self.assertIn(cry, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Cash")
            self.assertIn(csh, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Automobile")
            self.assertIn(atm, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Electronic")
            self.assertIn(elc, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Phone")
            self.assertIn(phn, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Laptop")
            self.assertIn(lpt, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Other")
            self.assertIn(oth, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Jewelry")
            self.assertIn(jwy, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all LandedProperty")
            self.assertIn(lnd, f.getvalue())

    def test_create_command_with_kwargs(self):
        """Test create command with kwargs."""
        # Test create command with additional key-value pairs
        with patch("sys.stdout", new=StringIO()) as f:
            call = (f'create FingerPrint name="My_fingerprint"') 
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()
         # Test if the created instance and kwargs are in the
         #    output of "all" command
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all FingerPrint")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'name': 'My fingerprint'", output)


if __name__ == "__main__":
    unittest.main()
