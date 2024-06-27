#!/usr/bin/python3
""" State Module for HBNB project """

from models import db
from models.variables import recovery_statuses, top_currencies

class Recovery(db.Model):
    """A fingerprint object that defines each suspects fingerprint"""
    
    __tablename__ = 'recoveries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    petition_id = db.Column(db.String(50), db.ForeignKey('petitions.casefile_no'), nullable=False)
    suspect_id = db.Column(db.Integer, db.ForeignKey('suspects.id'), nullable=False)
    
    monetaries = db.relationship('Monetary', backref='recovery', cascade="all, delete-orphan")
    automobilies = db.relationship('Automobile', backref='recovery', cascade="all, delete-orphan")
    electronics = db.relationship('Electronic', backref='recovery', cascade="all, delete-orphan")
    jewelries = db.relationship('Jewelry', backref='recovery', cascade="all, delete-orphan")
    landedproperties = db.relationship('LandedProperty', backref='recovery', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Recovery(id={self.id}, petition_id='{self.petition_id}')>"

    def __str__(self):
        return f"Recovery {self.id} for Petition {self.petition_id}"

class Monetary(db.Model):
    """A table that contains features of monetary recoveries"""
    
    __tablename__ = 'monetaries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Enum(*recovery_statuses), nullable=False)
    recovery_id = db.Column(db.Integer, db.ForeignKey('recoveries.id'))

    banks = db.relationship('Bank', backref='monetary', cascade="all, delete-orphan")
    cryptos = db.relationship('Crypto', backref='monetary', cascade="all, delete-orphan")
    cashes = db.relationship('Cash', backref='monetary', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Monetary(id={self.id}, status='{self.status}')>"

    def __str__(self):
        return f"Monetary Recovery {self.id} with status {self.status}"

class Bank(db.Model):
    """Blueprint of Bank monetary recoveries"""
    
    __tablename__ = 'bank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bank_name = db.Column(db.String(50))
    serial_number = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    favour_off = db.Column(db.String(20))
    monetary_id = db.Column(db.Integer, db.ForeignKey('monetaries.id'), nullable=False)

    def __repr__(self):
        return f"<Bank(id={self.id}, bank_name='{self.bank_name}')>"

    def __str__(self):
        return f"Bank Recovery {self.id} from {self.bank_name}"

class Crypto(db.Model):
    """Blueprint of crypto recoveries"""
    
    __tablename__ = 'crypto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_name = db.Column(db.String(50))
    asset_size = db.Column(db.String(50))
    asset_worth = db.Column(db.Integer)
    monetary_id = db.Column(db.Integer, db.ForeignKey('monetaries.id'), nullable=False)

    def __repr__(self):
        return f"<Crypto(id={self.id}, asset_name='{self.asset_name}')>"

    def __str__(self):
        return f"Crypto Recovery {self.id} of {self.asset_name}"

class Cash(db.Model):
    """Blueprint for cash recovered"""
    
    __tablename__ = 'cash'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    denomination = db.Column(db.Enum(*top_currencies), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    monetary_id = db.Column(db.Integer, db.ForeignKey('monetaries.id'))

    def __repr__(self):
        return f"<Cash(id={self.id}, denomination='{self.denomination}')>"

    def __str__(self):
        return f"Cash Recovery {self.id} of {self.amount} {self.denomination}"

class Automobile(db.Model):
    """A table that contains features of automobile recoveries"""
    
    __tablename__ = 'automobile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200))
    plate_number = db.Column(db.String(10))
    chasis_number = db.Column(db.String(50))
    colar = db.Column(db.String(20))
    other_info = db.Column(db.String(128))
    status = db.Column(db.Enum(*recovery_statuses), nullable=False)
    recovery_id = db.Column(db.Integer, db.ForeignKey('recoveries.id'), nullable=False)

    def __repr__(self):
        return f"<Automobile(id={self.id}, description='{self.description}')>"

    def __str__(self):
        return f"Automobile Recovery {self.id} described as {self.description}"

class Electronic(db.Model):
    """A table that contains features of electronic recoveries"""
    
    __tablename__ = 'electronics'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Enum(*recovery_statuses), nullable=False)
    recovery_id = db.Column(db.Integer, db.ForeignKey('recoveries.id'), nullable=False)
    
    # Relationships
    phones = db.relationship('Phone', backref='electronic', cascade="all, delete-orphan")
    laptops = db.relationship('Laptop', backref='electronic', cascade="all, delete-orphan")
    others = db.relationship('Other', backref='electronic', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Electronic(id={self.id}, status='{self.status}')>"

    def __str__(self):
        return f"Electronic Recovery {self.id} with status {self.status}"

class Phone(db.Model):
    """Blueprint of phone recoveries"""
    
    __tablename__ = 'phones'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20))
    imei = db.Column(db.String(50))
    electronic_id = db.Column(db.Integer, db.ForeignKey('electronics.id'))

    def __repr__(self):
        return f"<Phone(id={self.id}, phone_name='{self.phone_name}')>"

    def __str__(self):
        return f"Phone Recovery {self.id} named {self.phone_name}"

class Laptop(db.Model):
    """Blueprint for laptop recoveries"""
    
    __tablename__ = 'laptop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_no = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20))
    name = db.Column(db.String(50))
    electronic_id = db.Column(db.Integer, db.ForeignKey('electronics.id'))

    def __repr__(self):
        return f"<Laptop(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Laptop Recovery {self.id} named {self.name}"

class Other(db.Model):
    """Blueprint for other recoveries"""
    
    __tablename__ = 'other'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128))
    electronic_id = db.Column(db.Integer, db.ForeignKey('electronics.id'))

    def __repr__(self):
        return f"<Other(id={self.id}, description='{self.description}')>"

    def __str__(self):
        return f"Other Electronic Recovery {self.id} described as {self.description}"

class Jewelry(db.Model):
    """A table that contains features of jewelry recoveries"""
    
    __tablename__ ='jewelry'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(128))
    status = db.Column(db.Enum(*recovery_statuses), nullable=False)
    recovery_id = db.Column(db.Integer, db.ForeignKey('recoveries.id'), nullable=False)

    def __repr__(self):
        return f"<Jewelry(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Jewelry Recovery {self.id} named {self.name}"

class LandedProperty(db.Model):
    """A table that contains features of landed properties recoveries"""
    
    __tablename__ = 'landedproperty'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer)
    status = db.Column(db.Enum(*recovery_statuses), nullable=False)
    recovery_id = db.Column(db.Integer, db.ForeignKey('recoveries.id'))

    def __repr__(self):
        return f"<LandedProperty(id={self.id}, location='{self.location}')>"

    def __str__(self):
        return f"Landed Property Recovery {self.id} located at {self.location}"
