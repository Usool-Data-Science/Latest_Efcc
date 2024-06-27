#!/usr/bin/python3
from models import db
from models.variables import nigeria_states

# Association table for petitions and complainants
association_pet_comp = db.Table(
    "petition_complainant",
    db.Column("petition_id", db.ForeignKey("petitions.id"), primary_key=True, nullable=False),
    db.Column("complainant_id", db.ForeignKey("complainants.id"), primary_key=True, nullable=False)
)

class Complainant(db.Model):
    """A complainant object that defines each complainant's features"""

    __tablename__ = 'complainants'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.VARCHAR(128), nullable=False)
    nationality = db.Column(db.String(20), default="Nigerian", nullable=False)
    state = db.Column(db.Enum(*nigeria_states), nullable=False)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    religion = db.Column(db.Enum('Islam', 'Christianity', 'Traditional', 'Others'), nullable=False)
    education = db.Column(db.Enum('Primary', 'Secondary', 'Tertiary'), nullable=False)
    phone_no = db.Column(db.VARCHAR(15), nullable=False)
    
    # Define relationships
    suspects = db.relationship("Suspect", secondary="complainant_suspect", viewonly=False, back_populates="complainants")
    petitions = db.relationship("Petition", secondary="petition_complainant", viewonly=False, back_populates="complainants")

    def __repr__(self):
        return f"<Complainant(id={self.id}, name={self.name})>"

    def __str__(self):
        return f"Complainant: {self.name}, Phone: {self.phone_no}, State: {self.state}"
