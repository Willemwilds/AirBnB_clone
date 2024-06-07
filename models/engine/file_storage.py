import json

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
         if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        with open (self.__file_path, 'w', encoding="UFT-8") as f:
            return json.dump(f, self.__objects)
        
    def reload(self):
        with open (self.__file_path, 'w', encoding="UFT-8") as f:
            if f:
                return json.load(f, self.__objects)
            else:
                pass