"""filestorage class that serializes instances to a JSON file and deeserializes JSON file to instances"""

import json



class FileStorage:
    """private class attribute"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects, the obj key with key <obj  class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj
        

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for obj in self.__objects:
            new_dict[obj] = self.__objects[obj].to_dict()

        with open(self.__file_path, "w") as fd:
            json.dump(new_dict, fd)


    def reload(self):
        from models.base_model import BaseModel
        from models.user import User 
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
       
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exist"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = eval(val['__class__'])(**val)
        except FileNotFoundError:
            pass