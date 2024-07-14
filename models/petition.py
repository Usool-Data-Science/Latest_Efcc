#!/usr/bin/python3
""" Place Module for HBNB project """
from models import db
from datetime import datetime
from flask_login import UserMixin
from models.recovery import Recovery
from models.suspect import Suspect
from models.base_model import BaseModel
from models.variables import petition_status


# association_pet_recov = db.Table("petition_recovery",
#     db.Column("petition_id", db.ForeignKey("petitions.id"), primary_key=True, nullable=False),
#     db.Column("recovery_id", db.ForeignKey("recoveries.id"), primary_key=True, nullable=False)
# )
# association_pet_susp = db.Table("petition_suspect",
#     db.Column("petition_id", db.ForeignKey("petitions.id"), primary_key=True, nullable=False),
#     db.Column("suspect_id", db.ForeignKey("suspects.id"), primary_key=True, nullable=False)
# )

class Petition(BaseModel, db.Model, UserMixin):
    """
        A blueprint for the petition model
    """
    __tablename__ = 'petitions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    casefile_no = db.Column(db.String(50), nullable=False)
    cr_no = db.Column(db.String(50), nullable=False)
    date_received = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_assigned = db.Column(db.DateTime, nullable=False, default=datetime.now)
    amount_involved = db.Column(db.Integer, default=0)
    status_signal = db.Column(db.Enum(*petition_status))
    petition_source = db.Column(db.Enum('Intelligence', 'Regular-Complain'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)

    recoveries = db.relationship("Recovery", viewonly=False, back_populates="petition", cascade="all, delete-orphan")
    suspects = db.relationship("Suspect", viewonly=False, back_populates="petition", cascade="all, delete-orphan")
    complainants = db.relationship("Complainant", viewonly=False, back_populates="petition", cascade="all, delete-orphan")
    staff = db.relationship("Staff", viewonly=False, back_populates="petitions")
    # suspects = db.relationship("Suspect", secondary="petition_suspect", viewonly=False, back_populates="petitions")
    # complainants = db.relationship("Complainant", secondary="petition_complainant", viewonly=False, back_populates="petitions")
    # staffs = db.relationship("Staff", secondary="petition_staff", viewonly=False, back_populates="petitions")

    def __repr__(self):
        return f"<Petition(id={self.id}, casefile_no='{self.casefile_no}', cr_no='{self.cr_no}')>"

    def __str__(self):
        return f"Petition {self.casefile_no} ({self.cr_no})"