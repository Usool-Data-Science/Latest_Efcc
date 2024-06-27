#!/usr/bin/python3
from models import db

class FingerPrint(db.Model):
    """
    A fingerprint object that defines each suspect's fingerprint and associated mugshot.

    Attributes:
        id (int): The primary key for the fingerprint record.
        finger_print (str): The fingerprint data.
        mugshot (str): The path to the suspect's mugshot image. This will be changed to BLOB later.
        suspect_id (int): The foreign key linking to the suspect's ID.
    """

    __tablename__ = 'fingerprints'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    finger_print = db.Column(db.String(128), nullable=False)
    mugshot = db.Column(db.String(128), nullable=False)  # Change this later to BLOB
    suspect_id = db.Column(db.Integer, db.ForeignKey('suspects.id'), nullable=False)

    # def __repr__(self):
    #      return f"<FingerPrint(id={self.id}, suspect_id={self.suspect_id}, finger_print='{self.finger_print}')>"

    # def __str__(self):
    #      return f"FingerPrint for Suspect ID {self.suspect_id}: {self.finger_print}"

