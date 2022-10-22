"""Base model that defines all common attributes/methods for other classess"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        if (kwargs):
            for  key,value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            
   

    def __str__(self):
        """ print a representation in readeable format"""
        return "[{}]  ({}) {} ".format(self.__class__.__name__, self.id,  self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at  = datetime.now()
        storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__ of the instance"""
        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict["__class__"]  = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

