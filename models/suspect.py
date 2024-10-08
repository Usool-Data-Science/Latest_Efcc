#!/usr/bin/python3
""" Review module for the HBNB project """

from models import db
from models.base_model import BaseModel
from models.complainant import Complainant
from models.identity import Identity
from models.fingerprint import FingerPrint
from models.variables import nigeria_skin_colors, religion_types, offence_types

association_feud = db.Table("complainant_suspect",
    db.Column("complainant_id", db.ForeignKey("complainants.id"), primary_key=True, nullable=False),
    db.Column("suspect_id", db.ForeignKey("suspects.id"), primary_key=True, nullable=False)
)

association_id_susp = db.Table("identity_suspect",
    db.Column("idenitity_id", db.ForeignKey("identities.id"), primary_key=True, nullable=False),
    db.Column("suspect_id", db.ForeignKey("suspects.id"), primary_key=True, nullable=False)
)

association_finger_susp = db.Table("finger_suspect",
    db.Column("finger_print_id", db.ForeignKey("fingerprints.id"), primary_key=True, nullable=False),
    db.Column("suspect_id", db.ForeignKey("suspects.id"), primary_key=True, nullable=False)
)


class Suspect(BaseModel, db.Model):
    """A suspect object that defines each suspect's features"""  
    
    __tablename__ = 'suspects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    skin_color = db.Column(db.Enum(*nigeria_skin_colors), default='Dark')
    passport = db.Column(db.String, nullable=False)
    mugshot = db.Column(db.String, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(20), default="Nigerian")
    place_of_birth = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)
    religion = db.Column(db.Enum(*religion_types), nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    offence = db.Column(db.Enum(*offence_types), nullable=False)
    petition_id = db.Column(db.Integer, db.ForeignKey("petitions.id"), nullable=False)

    # Relationships
    identities = db.relationship("Identity", secondary="identity_suspect", viewonly=False, back_populates="suspect")
    finger_prints = db.relationship("FingerPrint", secondary="finger_suspect", viewonly=False, back_populates="suspect")
    recoveries = db.relationship("Recovery", cascade="all, delete-orphan", backref="suspects")
    petition = db.relationship("Petition", viewonly=False, back_populates="suspects")
    complainants = db.relationship("Complainant", secondary="complainant_suspect", viewonly=False, back_populates="suspects")

    def __repr__(self):
        return f"<Suspect(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Suspect {self.id} named {self.name}"
