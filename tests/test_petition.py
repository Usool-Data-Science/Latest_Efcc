#!/usr/bin/python3
import unittest
import os
import uuid
from models import Base
from dotenv import load_dotenv
from models.petition import Petition
from models.fingerprint import FingerPrint
from models.complainant import Complainant
from models.identity import Identity
from models.suspect import Suspect
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models.recovery import (Recovery, Monetary, Bank, Crypto,
                                          Automobile, Electronic, Phone,
                                          Laptop, Other, Jewelry, LandedProperty)

class TestPetition(unittest.TestCase):
    """A blueprint for testing the petition object"""
    @classmethod
    def setUpClass(cls):
        """ds"""
        # Load Environment variables
        load_dotenv()
        EFCC_MYSQL_USER = os.getenv("EFCC_MYSQL_USER")
        EFCC_MYSQL_PWD = os.getenv("EFCC_MYSQL_PWD")
        EFCC_MYSQL_HOST = os.getenv("EFCC_MYSQL_HOST")
        EFCC_MYSQL_DB = os.getenv("EFCC_MYSQL_DB")

        # Create Engine
        uri = "mysql+mysqldb://{}:{}@{}/{}".format(EFCC_MYSQL_USER, EFCC_MYSQL_PWD,
                                                   EFCC_MYSQL_HOST, EFCC_MYSQL_DB)
        cls.engine = create_engine(uri)
        cls.session = sessionmaker(cls.engine)()
        
        cls.pet_no = uuid.uuid4()
    	# Initialize the sample models
        cls.example_suspect = Suspect(name='John Doe', height=175, skin_color='Dark Brown',
                                                  passport=b'\x00\x01\x02...', mugshot=b'\x00\x01\x02...',
                          address='123 Main Street, Lagos', place_of_birth='Lagos',                          gender='Male', religion='Christianity', occupation='Engineer',
                          phone_no='08012345678', parent_name='Jane Doe',
                           petition_no=cls.pet_no)
        cls.example_complainant = Complainant(name='Jane Smith', address='456 Oak Street, Abuja',
                                          nationality='Nigerian', state='Lagos', gender='Female',
                                          age=35, occupation='Teacher', religion='Christianity',
                                          education='Tertiary', phone_no='08098765432',
                                           petition_no=cls.pet_no)
        cls.example_fingerprint = FingerPrint(finger_print='A9C2F0B4E7D5',
                                          mugshot=b'\x00\xFF\x80\xFF\x80\x00',
                                           petition_no=cls.pet_no)
        cls.example_petition = Petition(casefile_no=cls.pet_no,
                                    cr_no='CR123456', date_received=datetime.utcnow(),
                                    date_assigned=datetime.utcnow(), amount_involved=500000,
                                    status_signal='In-Progress', petition_source='Regular-Complain')
        cls.example_identity = Identity(id_types='NIN', id_number='1234567890',
                                     petition_no=cls.pet_no)
        # Create Recovery Instance
        cls.example_recovery = Recovery()
        # Create Monetary instances
        cls.example_monetary_1 = Monetary(status='With Exhibit keeper')
        cls.example_monetary_2 = Monetary(status='Tendered in Court')
        # Create Bank instances associated with monetary_instance_1
        cls.example_bank_1 = Bank(bank_name='First Bank', serial_number=1234, amount=500000, favour_off='John Doe')
        cls.example_bank_2 = Bank(bank_name='GTBank', serial_number=5678, amount=800000, favour_off='Jane Smith')
        # Create Crypto instances associated with monetary_instance_2
        cls.example_crypto_1 = Crypto(asset_name='Bitcoin', asset_size='10 BTC', asset_worth=2000000)
        cls.example_crypto__2 = Crypto(asset_name='Ethereum', asset_size='15 ETH', asset_worth=1500000)
        # Create an instance of Automobile
        cls.example_automobile = Automobile(description='Toyota Corolla', plate_number='ABC123', chasis_number='XYZ456',
                                         colar='Blue', other_info='Good condition', status='Interim forfeiture')
        # Create instances of Electronic
        cls.example_electronic = Electronic(status='Final Forfeiture')
        # Create instances of Phone associated with electronic_instance
        cls.example_phone_1 = Phone(phone_name='iPhone 12', color='Black', imei='123456789012345')
        cls.example_phone_2 = Phone(phone_name='Samsung Galaxy S20', color='White', imei='987654321098765')
        # Create instances of Laptop associated with electronic_instance
        cls.example_laptop_1 = Laptop(serial_no='LAP001', color='Silver', name='HP Pavilion')
        cls.example_laptop_2= Laptop(serial_no='LAP002', color='Space Grey', name='MacBook Pro')
        # Create instances of Other associated with electronic_instance
        cls.example_other_1 = Other(description='Smartwatch')
        cls.example_other_2 = Other(description='Bluetooth speaker')
        # Create an instance of Jewelry
        cls.example_jewelry = Jewelry(name='Gold necklace', description='18K gold necklace', status='With Exhibit keeper')
        # Create an instance of LandedProperty
        cls.example_landed_property = LandedProperty(location='Lagos', size=500, status='Final Forfeiture')
        
        cls.session.add_all([cls.example_complainant, cls.example_fingerprint,
                 cls.example_petition, cls.example_identity, cls.example_suspect,
                 cls.example_monetary_1, cls.example_bank_1, cls.example_crypto_1,
                 cls.example_automobile, cls.example_electronic, cls.example_phone_1,
                 cls.example_laptop_1, cls.example_other_1, cls.example_jewelry,
                 cls.example_landed_property, cls.example_recovery])
        cls.session.commit()
        
    @classmethod    
    def tearDownClass(cls):
        """Disposes the engine after completion of the whole transaction"""
        cls.session.rollback()
        cls.session.close()
        cls.engine.dispose()
    
    def test_petition_attributes(self):
        """Test the initialization of the models"""
        self.assertEqual(self.example_petition.casefile_no, str(self.pet_no))
        self.assertEqual(self.example_petition.cr_no, 'CR123456')
        self.assertIsInstance(self.example_petition.date_received, datetime)
        self.assertIsInstance(self.example_petition.date_assigned, datetime)
        self.assertEqual(self.example_petition.amount_involved, 500000)
        self.assertEqual(self.example_petition.status_signal, 'In-Progress')
        self.assertEqual(self.example_petition.petition_source, 'Regular-Complain')	
        
    def test_relationship(self):
        """
            Tests for relationship between petition and other tables
            1. Add the relationships to the petition table
            2. Commit the relationship
            3. Check if the relationship are added to the petition table.
            4. Query one petition and confirm if the relationship is in the list.
        """
        self.example_petition.fingerprints.append(self.example_fingerprint)
        self.example_petition.complainants.append(self.example_complainant)
        self.example_petition.suspects.append(self.example_suspect)
        self.example_petition.recoveries.append(self.example_recovery)
        
        self.session.add(self.example_petition)
        self.session.commit()
        
        # Check if the relationship i correctly added
        self.assertTrue(self.example_petition.fingerprints)
        self.assertTrue(self.example_petition.complainants)
        self.assertTrue(self.example_petition.suspects)
        self.assertTrue(self.example_petition.recoveries)

        # Check if the relationship is correct
        petition1 = self.session.query(Petition).filter(
            Petition.casefile_no==str(self.pet_no)).first()
        self.assertIn(self.example_fingerprint, petition1.fingerprints)
        self.assertIn(self.example_complainant, petition1.complainants)
        self.assertIn(self.example_suspect, petition1.suspects)
        self.assertIn(self.example_recovery, petition1.recoveries)
                
        
if __name__ == '__main__':
    unittest.main()
