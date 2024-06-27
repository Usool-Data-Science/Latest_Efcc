#!/usr/bin/python3
""" Place Module for HBNB project """
from models import db
from datetime import datetime
from flask_login import UserMixin
from models.recovery import Recovery
from models.suspect import Suspect


association_pet_susp = db.Table("petition_suspect",
    db.Column("petition_id", db.ForeignKey("petitions.id"), primary_key=True, nullable=False),
    db.Column("suspect_id", db.ForeignKey("suspects.id"), primary_key=True, nullable=False)
)

class Petition(db.Model, UserMixin):
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
    status_signal = db.Column(db.Enum('Convicted', 'In-Progress'))
    petition_source = db.Column(db.Enum('Intelligence', 'Regular-Complain'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staffs.id'), nullable=False)

    recoveries = db.relationship("Recovery", cascade="all, delete-orphan", backref="petitions")
    suspects = db.relationship("Suspect", secondary="petition_suspect", viewonly=False, back_populates="petitions")
    complainants = db.relationship("Complainant", secondary="petition_complainant", viewonly=False, back_populates="petitions")
    staffs = db.relationship("Staff", secondary="petition_staff", viewonly=False, back_populates="petitions")

    def __repr__(self):
        return f"<Petition(id={self.id}, casefile_no='{self.casefile_no}', cr_no='{self.cr_no}')>"

    def __str__(self):
        return f"Petition {self.casefile_no} ({self.cr_no})"