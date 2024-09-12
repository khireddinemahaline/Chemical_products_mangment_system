#!/usr/bin/python3
"""
BaseModel
    basemodel is for generating ids and datedate for deffrent classes
    id : string(60) # uuid.uuid4()
    created_at : datetime() # from datetime import datetime
    updated_at : datetime # the time update # strftime("%Y-%m-%d %H:%M:%S")
- all  other classes will inhert from the BaseModel class
- we will store data in mysql_DBMS
    * to store the data we will use a python library (sqlalchemy)
"""

from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
Base = declarative_base()


class BaseModel():
    """
    BaseModel
        id : the UUID of the class instance.
        created_at : the timestamp when the instance was created.
        updated_at : the timestamp when the instance was last updated.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        re-create an instance with this dictionary representation.
            className(**dic)
        """
        self.id = str(uuid.uuid4())  # Generate a new UUID
        self.created_at = datetime.now()  # Set creation time
        self.updated_at = datetime.now()  # Set last update time
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        cls = type(self).__name__
        attributes = ', '.join(
            "'{}':{}".format(key, repr(getattr(self, key)))
            for key in self.__dict__.keys()
            if key != '_sa_instance_state'
        )
        return "[{}] ('{}') {{{}}}".format(cls, self.id, attributes)

    def save(self):
        self.updated_at = datetime.now()  # update time
        models.storage.new(self)  # add to storage
        models.storage.save()  # commit changes

    def to_dict(self):
        dic_obj = {}
        dic_obj.update(self.__dict__)  # Copy instance dictionary
        if '_sa_instance_state' in dic_obj:
            del dic_obj['_sa_instance_state']  # Remove SQLAlchemy state
        if '_password' in dic_obj:
            del dic_obj['_password']
        dic_obj.update({
            '__class__': type(self).__name__,  # Add class name
            'created_at': self.created_at.isoformat(),  # Format date as ISO
            'updated_at': self.updated_at.isoformat()
        })
        return dic_obj

    def delete(self):

        models.storage.delete(self)  # close session
