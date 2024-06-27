#!/usr/bin/python3
"""This module defines a class Identity"""
from models import db
from models.variables import id_cards

class Identity(db.Model):
    """
        A blueprint for the supsect identification
    """
    __tablename__ = 'identities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_types = db.Column(db.Enum(*id_cards), nullable=False)
    id_number = db.Column(db.Integer, nullable=False)

    # Relationships
    suspect_id = db.Column(db.Integer, db.ForeignKey('suspects.id'), nullable=False)

    def __repr__(self):
        return f"<Identity(id={self.id}, id_type='{self.id_types}', id_number={self.id_number}, suspect_id={self.suspect_id})>"

    def __str__(self):
        return f"Identity {self.id_types}: {self.id_number} for Suspect ID {self.suspect_id}"

