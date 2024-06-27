#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

"""Standard libraries"""
from datetime import datetime

"""Third part libraries"""
from models import db

class BaseModel:
    """A base class for all EFCC models"""
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == 'updated_at' or k == 'created_at':
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k != '__class__' and hasattr(self.__class__, k):
                    setattr(self, k, v)
            if '__class__' in kwargs:
                del kwargs['__class__']

    def to_dict(self):
        """Convert instance into dict format"""
        s_dict = self.__dict__.copy()
        s_dict["__class__"] = type(self).__name__
        for key, value in s_dict.items():
            if isinstance(value, datetime):
                s_dict[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        try:
            s_dict.pop('_sa_instance_state')
        except Exception:
            pass
        return s_dict
    
    # def to_dict(self):
    #     return {column.name: getattr(self, column.name) for column in self.__table__.columns}