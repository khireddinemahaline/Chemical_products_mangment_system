#!/usr/bin/python3
"""
DBStorage
Manages interactions with a MySQL database using SQLAlchemy.
Provides methods for CRUD operations and session management.
    __engine : The Engine is responsible for managing the connection
               to the database
    __session : responsible for all the ORM operations
                like querying, adding, updating, and deleting records
"""
import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from dotenv import load_dotenv
load_dotenv()


class DBStorage():
    """
    Store the data in mysql database using mysql
        - show all objects stored in the database
        - add new object
        - save object to the database
        - reload the database
        - delete object
        - close the session
    """
    __engine = None
    __session = None

    def __init__(self):
        """ create engine that will store objects """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db))
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        db_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                if obj.__class__.__name__ in models.classes:
                    db_dict[key] = obj
            return db_dict
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    for obj in objs:
                        key = "{}.{}".format(obj.__class__.__name__,
                                             obj.id)
                        db_dict[key] = obj
        return db_dict

    def new(self, obj):
        """add new object to the database"""
        if isinstance(obj, Base):
            self.__session.add(obj)

    def save(self):
        """Commit the current transaction."""
        try:
            self.__session.commit()
            print("Changes committed.")
        except Exception as e:
            self.__session.rollback()
            print(f"Failed to commit changes: {e}")

    def delete(self, obj):
        """delete an obj stored in the database"""
        if isinstance(obj, Base):
            self.__session.delete(obj)

    def reload(self):
        """create the tables and all column in database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """in the end close the session"""
        if self.__session:
            self.__session.close()

    def get(self, cls, id):
        """
        get the object dependes on the id
        cls.id => get this object from the storage
        """
        get_dic = self.all(cls)
        for key, value in get_dic.items():
            if id:
                if key == str(cls.__name__) + '.' + id:
                    return value
            else:
                return None
        return None

    def count(self, cls=None):
        """
        count the number of object have:
            if cls : objects with the same class name
            else : all object in the storage
        """
        count = 0
        if cls:
            get_dic = self.all(cls)
            for keys, value in get_dic.items():
                key = keys.split('.')[0]
                if key == str(cls.__name__):
                    count = count + 1
            return count
        else:
            get_dic = self.all()
            for keys, value in get_dic.items():
                count = count + 1
            return count
