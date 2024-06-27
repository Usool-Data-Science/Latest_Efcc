#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

"""Standard libraries"""
import uuid
from datetime import datetime

"""Third part libraries"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer
# from flask_sqlachemy import SQLAlchemy

Base = declarative_base()

class BaseModel:
    """A base class for all EFCC models"""
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage
        # self.id = str(uuid.uuid4())
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
            # self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        # from models import storage
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

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

    def delete(self):
        """
        Deletes the instance of the object from the storage
            We Import storage directly here to avoid circular
            import errors.
        """
        # from models import storage
        from models import storage
        storage.delete(self)
        storage.save()
