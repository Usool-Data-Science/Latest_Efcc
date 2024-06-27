#!/usr/bin/python3
import json
from datetime import datetime
from models import app, db
from models.complainant import Complainant
from models.suspect import Suspect
from models.fingerprint import FingerPrint
from models.identity import Identity
from models.petition import Petition
from models.staff import Staff
from models.recovery import (Monetary, Bank, Crypto, Cash, Recovery,
                                Electronic, Phone, Laptop, Other,
                                Automobile, Jewelry, LandedProperty)

with app.app_context():
    db.create_all()

# Create and save 5 instances of Suspect
suspect1 = Suspect(name="John Doe", height=180, skin_color="Brown", 
                   passport="passport1", mugshot="mugshot1",
                   address="Address 1", nationality="Nigerian",
                    place_of_birth="City 1", gender="Male",
                   religion="Christianity", occupation="Occupation 1",
                    phone_no="123456789", parent_name="Parent 1",
                    offence="Theft")


suspect2 = Suspect(name="Jane Smith", height=170, skin_color="Fair", passport="passport2", mugshot="mugshot2",
                   address="Address 2", nationality="Nigerian", place_of_birth="City 2", gender="Female", religion="Islam", occupation="Occupation 2", phone_no="987654321", parent_name="Parent 2", offence="Forgery")


suspect3 = Suspect(name="Michael Johnson", height=175, skin_color="Dark Brown", passport="passport3", mugshot="mugshot3",
                   address="Address 3", nationality="Nigerian", place_of_birth="City 3", gender="Male", religion="Traditional", occupation="Occupation 3", phone_no="456123789", parent_name="Parent 3", offence="Bribery")


suspect4 = Suspect(name="Alice Brown", height=160, skin_color="Light Brown", passport="passport4", mugshot="mugshot4",
                   address="Address 4", nationality="Nigerian", place_of_birth="City 4", gender="Female", religion="Christianity", occupation="Occupation 4", phone_no="789456123", parent_name="Parent 4", offence="Stealing")


suspect5 = Suspect(name="David Wilson", height=185, skin_color="Caramel", passport="passport5", mugshot="mugshot5",
                   address="Address 5", nationality="Nigerian", place_of_birth="City 5", gender="Male", religion="Others", occupation="Occupation 5", phone_no="321987654", parent_name="Parent 5", offence="Impersonation")
db.session.add_all([suspect1, suspect2, suspect3, suspect4, suspect5])
db.session.commit() 


# Create and save 5 instances of Complainant
complainant1 = Complainant(name="John Smith", address="123 Main St", nationality="Nigerian", state="Lagos", gender="Male",
                           age=35, occupation="Engineer", religion="Christianity", education="Tertiary", phone_no="1234567890")


complainant2 = Complainant(name="Jane Doe", address="456 Oak St", nationality="Nigerian", state="Abuja", gender="Female",  
                           age=28, occupation="Doctor", religion="Islam", education="Tertiary", phone_no="2345678901")


complainant3 = Complainant(name="Michael Johnson", address="789 Elm St", nationality="Nigerian", state="Rivers",
                           gender="Male", age=42, occupation="Lawyer", religion="Traditional", education="Secondary", phone_no="3456789012")


complainant4 = Complainant(name="Emily Brown", address="101 Pine St", nationality="Nigerian", state="Enugu", gender="Female", 
                           age=30, occupation="Teacher", religion="Christianity", education="Primary", phone_no="4567890123")


complainant5 = Complainant(name="David Wilson", address="222 Maple St", nationality="Nigerian", state="Ogun", gender="Male", 
                           age=50, occupation="Businessman", religion="Others", education="Secondary", phone_no="5678901234")
db.session.add_all([complainant1, complainant2, complainant3, complainant4, complainant5])
db.session.commit() 


# Create and save 5 instances of FingerPrint
fingerprint1 = FingerPrint(finger_print="fingerprint1", mugshot="mugshot1", suspect_id=suspect1.id)


fingerprint2 = FingerPrint(finger_print="fingerprint2", mugshot="mugshot2", suspect_id=suspect2.id)


fingerprint3 = FingerPrint(finger_print="fingerprint3", mugshot="mugshot3", suspect_id=suspect3.id)


fingerprint4 = FingerPrint(finger_print="fingerprint4", mugshot="mugshot4", suspect_id=suspect4.id)


fingerprint5 = FingerPrint(finger_print="fingerprint5", mugshot="mugshot5", suspect_id=suspect5.id)
db.session.add_all([fingerprint1, fingerprint2, fingerprint3, fingerprint4, fingerprint5])
db.session.commit() 


# Create the first instance of Staff
staff1 = Staff(
    first_name="Adeshina",
    last_name="Ibrahim",
    email="adeshinaibrahim10@gmail.com",
    password="hashed_password_1",
    age=30,
    state="Lagos"
)


# Create the second instance of Staff
staff2 = Staff(
    first_name="Oluwatobi",
    last_name="Olatunde",
    email="oluwatobiolatunde@example.com",
    password="hashed_password_2",
    age=28,
    state="Ogun"
)
db.session.add_all([staff1, staff2])
db.session.commit() 

# Create and save 5 instances of Petition
petition1 = Petition( casefile_no="CASE1", cr_no="CR1", date_received=datetime.now(), date_assigned=datetime.now(),
                     amount_involved=1000, status_signal='In-Progress', staff_id=staff1.id, petition_source='Regular-Complain')


petition2 = Petition(casefile_no="CASE2", cr_no="CR2", date_received=datetime.now(), date_assigned=datetime.now(),
                     amount_involved=2000, status_signal='In-Progress', staff_id=staff1.id, petition_source='Regular-Complain')


petition3 = Petition(casefile_no="CASE3", cr_no="CR3", date_received=datetime.now(), date_assigned=datetime.now(),
                     amount_involved=3000, status_signal='In-Progress', staff_id=staff1.id, petition_source='Regular-Complain')


petition4 = Petition(casefile_no="CASE4", cr_no="CR4", date_received=datetime.now(), date_assigned=datetime.now(),
                     amount_involved=4000, status_signal='In-Progress', staff_id=staff2.id, petition_source='Regular-Complain')


petition5 = Petition(casefile_no="CASE5", cr_no="CR5", date_received=datetime.now(), date_assigned=datetime.now(),
                     amount_involved=5000, status_signal='In-Progress', staff_id=staff2.id, petition_source='Regular-Complain')
db.session.add_all([petition1, petition2, petition3, petition4, petition5])
db.session.commit() 

# Create instances of Recovery class
recovery1 = Recovery(
    petition_id="CASE1",
    suspect_id=suspect1.id
)



recovery2 = Recovery(
    petition_id="CASE2",
    suspect_id=suspect2.id
)



recovery3 = Recovery(
    petition_id="CASE3",
    suspect_id=suspect3.id
)



recovery4 = Recovery(
    petition_id="CASE4",
    suspect_id=suspect4.id
)



recovery5 = Recovery(
    petition_id="CASE5",
    suspect_id=suspect5.id
)
db.session.add_all([recovery1, recovery2, recovery3, recovery4, recovery5])
db.session.commit() 


# Create instances of Monetary class
monetary1 = Monetary(
    status='With Exhibit keeper',
    recovery_id=recovery1.id
)



monetary2 = Monetary(
    status='Tendered in Court',
    recovery_id=recovery2.id
)



monetary3 = Monetary(
    status='Interim forfeiture',
    recovery_id=recovery3.id
)



monetary4 = Monetary(
    status='Final Forfeiture',
    recovery_id=recovery4.id
)



monetary5 = Monetary(
    status='Tendered in Court',
    recovery_id=recovery5.id
)
db.session.add_all([monetary1, monetary2, monetary3, monetary4, monetary5])
db.session.commit() 


# Create instances of Bank class
bank1 = Bank(
    bank_name='ABC Bank',
    serial_number=123456,
    amount=5000,
    favour_off='John Doe',
    monetary_id=monetary1.id
)



bank2 = Bank(
    bank_name='XYZ Bank',
    serial_number=654321,
    amount=7000,
    favour_off='Jane Smith',
    monetary_id=monetary2.id
)



bank3 = Bank(
    bank_name='PQR Bank',
    serial_number=987654,
    amount=8000,
    favour_off='Alice Brown',
    monetary_id=monetary3.id
)



bank4 = Bank(
    bank_name='LMN Bank',
    serial_number=456789,
    amount=6000,
    favour_off='Bob Johnson',
    monetary_id=monetary4.id
)



bank5 = Bank(
    bank_name='DEF Bank',
    serial_number=321654,
    amount=9000,
    favour_off='Charlie Wilson',
    monetary_id=monetary5.id
)
db.session.add_all([bank1, bank2, bank3, bank4, bank5])
db.session.commit() 


# Create instances of Automobile class
automobile1 = Automobile(
    description='Toyota Camry',
    plate_number='ABC123',
    chasis_number='1234567890',
    colar='Black',
    other_info='None',
    status='With Exhibit keeper',
    recovery_id=recovery1.id
)



automobile2 = Automobile(
    description='Honda Civic',
    plate_number='XYZ789',
    chasis_number='0987654321',
    colar='White',
    other_info='Scratched rear bumper',
    status='Tendered in Court',
    recovery_id=recovery2.id
)



automobile3 = Automobile(
    description='Ford Explorer',
    plate_number='PQR456',
    chasis_number='1357908642',
    colar='Red',
    other_info='Damaged windshield',
    status='Interim forfeiture',
    recovery_id=recovery3.id
)



automobile4 = Automobile(
    description='Chevrolet Malibu',
    plate_number='LMN321',
    chasis_number='2468013579',
    colar='Blue',
    other_info='None',
    status='Final Forfeiture',
    recovery_id=recovery4.id
)



automobile5 = Automobile(
    description='Nissan Altima',
    plate_number='DEF654',
    chasis_number='3698521470',
    colar='Silver',
    other_info='Dent on rear left fender',
    status='Tendered in Court',
    recovery_id=recovery5.id
)
db.session.add_all([automobile1, automobile2, automobile3, automobile4, automobile5])
db.session.commit() 


# Create instances of Electronic class
electronic1 = Electronic(
    status='With Exhibit keeper',
    recovery_id=recovery1.id
)



electronic2 = Electronic(
    status='Tendered in Court',
    recovery_id=recovery2.id
)



electronic3 = Electronic(
    status='Interim forfeiture',
    recovery_id=recovery3.id
)



electronic4 = Electronic(
    status='Final Forfeiture',
    recovery_id=recovery4.id
)



electronic5 = Electronic(
    status='Tendered in Court',
    recovery_id=recovery5.id
)
db.session.add_all([electronic1, electronic2, electronic3, electronic4, electronic5])
db.session.commit() 


# Create instances of Phone class
phone1 = Phone(
    phone_name='iPhone 12',
    color='Black',
    imei='123456789012345',
    electronic_id=electronic1.id
)



phone2 = Phone(
    phone_name='Samsung Galaxy S21',
    color='Silver',
    imei='987654321098765',
    electronic_id=electronic2.id
)



phone3 = Phone(
    phone_name='Google Pixel 5',
    color='White',
    imei='456789012345678',
    electronic_id=electronic3.id
)



phone4 = Phone(
    phone_name='OnePlus 9 Pro',
    color='Blue',
    imei='321098765432109',
    electronic_id=electronic4.id
)



phone5 = Phone(
    phone_name='Xiaomi Mi 11',
    color='Red',
    imei='654321098765432',
    electronic_id=electronic5.id
)
db.session.add_all([phone1, phone2, phone3, phone4, phone5])
db.session.commit() 


# Create instances of Jewelry class
jewelry1 = Jewelry(
    name='Diamond Necklace',
    description='18k gold with diamond pendant',
    status='With Exhibit keeper',
    recovery_id=recovery1.id
)



jewelry2 = Jewelry(
    name='Ruby Bracelet',
    description='Sterling silver with ruby gemstones',
    status='Tendered in Court',
    recovery_id=recovery2.id
)



jewelry3 = Jewelry(
    name='Emerald Ring',
    description='Platinum band with emerald stone',
    status='Interim forfeiture',
    recovery_id=recovery3.id
)



jewelry4 = Jewelry(
    name='Sapphire Earrings',
    description='White gold earrings with sapphire gems',
    status='Final Forfeiture',
    recovery_id=recovery4.id
)



jewelry5 = Jewelry(
    name='Pearl Necklace',
    description='Cultured pearl necklace with silver clasp',
    status='Tendered in Court',
    recovery_id=recovery5.id
)
db.session.add_all([jewelry1, jewelry2, jewelry3, jewelry4, jewelry5])
db.session.commit() 


# Create instances of LandedProperty class
landed_property1 = LandedProperty(
    location='123 Main Street, Cityville',
    size=1000,
    status='With Exhibit keeper',
    recovery_id=recovery1.id
)



landed_property2 = LandedProperty(
    location='456 Elm Street, Townsville',
    size=1500,
    status='Tendered in Court',
    recovery_id=recovery2.id
)



landed_property3 = LandedProperty(
    location='789 Oak Street, Villageton',
    size=2000,
    status='Interim forfeiture',
    recovery_id=recovery3.id
)



landed_property4 = LandedProperty(
    location='101 Pine Street, Hamletville',
    size=1800,
    status='Final Forfeiture',
    recovery_id=recovery4.id
)



landed_property5 = LandedProperty(
    location='111 Cedar Street, Townsburg',
    size=2200,
    status='Tendered in Court',
    recovery_id=recovery5.id
)
db.session.add_all([landed_property1, landed_property2, landed_property3, landed_property4, landed_property5])
db.session.commit() 

# Create instances of Identity class
identity1 = Identity(
    id_types='Licence',
    id_number=123456789,
    suspect_id=suspect1.id
)



identity2 = Identity(
    id_types='NIN',
    id_number=987654321,
    suspect_id=suspect2.id
)



identity3 = Identity(
    id_types='Passport',
    id_number=246813579,
    suspect_id=suspect3.id
)



identity4 = Identity(
    id_types='Licence',
    id_number=135792468,
    suspect_id=suspect4.id
)



identity5 = Identity(
    id_types='Passport',
    id_number=864207531,
    suspect_id=suspect5.id
)
db.session.add_all([identity1, identity2, identity3, identity4, identity5])
db.session.commit() 

# db.create_all()








staff1.petitions.extend([petition1, petition2, petition3])
staff2.petitions.extend([petition4, petition5])

# Link suspects and complainants to petition
petition1.suspects.extend([suspect1, suspect2, suspect3])
petition2.suspects.extend([suspect2, suspect5])
petition3.suspects.append(suspect3)
petition4.suspects.append(suspect4)
petition5.suspects.append(suspect5)
petition1.complainants.append(complainant1)
petition2.complainants.append(complainant2)
petition3.complainants.append(complainant3)
petition4.complainants.append(complainant4)
petition5.complainants.append(complainant5)

# Link petition and suspect to complainants
complainant1.suspects.append(suspect1)
complainant2.suspects.append(suspect2)
complainant3.suspects.append(suspect3)
complainant4.suspects.append(suspect4)
complainant5.suspects.append(suspect5)


db.session.commit()

print("OK!")

# db.session.add_all([crypto1, crypto2, crypto3, crypto4, crypto5])
# db.session.add_all([cash1, cash2, cash3, cash4, cash5])
# db.session.add_all([laptop1, laptop2, laptop3, laptop4, laptop5])
# db.session.add_all([other1, other2, other3, other4, other5])
