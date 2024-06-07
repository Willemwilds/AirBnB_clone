import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods 
    for other classes:
    """    
    def __init__(self,*args, **kwargs):
        
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self,key,value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at


    def _str__(self):
        """
        returns string representation for each instance created.
        """
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the public instance attribute updated_at 
        with the current datetime
        """
        self.updated_at = datetime.now

    def to_dict(self):
        """returns a dictionary containing all keys/values 
        of __dict__ of the instance
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result