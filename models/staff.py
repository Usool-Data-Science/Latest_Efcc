#!/usr/bin/python3

# Create the database models
from models import db
from models.variables import nigeria_states
from flask_login import UserMixin
from models.petition import Petition

association_pet_staff = db.Table("petition_staff",
    db.Column("petition_id", db.ForeignKey("petitions.id"), primary_key=True, nullable=False),
    db.Column("staff_id", db.ForeignKey("staffs.id"), primary_key=True, nullable=False)
)

class Staff(db.Model, UserMixin):
    """A Staff object that defines each Efcc staff features"""

    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Enum(*nigeria_states), nullable=False)

    # Relationship
    petitions = db.relationship("Petition", secondary="petition_staff", viewonly=False, back_populates="staffs")

    def __repr__(self):
        return f"<Staff(id={self.id}, email='{self.email}')>"

    def __str__(self):
        return f"Staff {self.first_name} {self.last_name}"
