#!/usr/bin/python3
"""Base class 1.0"""
import json


class Base:
    """class Base of all classes in project 0x0c"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to convert to json str repr"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """cls method to save json str to file """

        new_file = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is not None:
            for element in list_objs:
                list_dic.append(cls.to_dictionary(element))
        with open(new_file, mode="w", encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_dic))

    @classmethod
    def create(cls, **dictionary):
        """
            the class Base by adding the class method,
            returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            obj_j = cls(4, 5)
        else:
            obj_j = cls(6)
        obj_j.update(**dictionary)
        return(obj_j)

    @classmethod
    def load_from_file(cls):
        """
            Update the class Base by adding the class method,
            returns a list of instances
        """
        filename = cls.__name__ + '.json'

        try:
            list_ins = []
            with open(filename, encoding="utf-8") as file:
                dic = Base.from_json_string(file.read())
                for item in dic:
                    list_ins += [cls.create(**item)]
                return list_ins
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            pdate the class Base by adding the static method,
            that opens a window and draws all the Rectangles and Squares
        """
        csvfile = '{}.csv'.format(cls.__name__)
        with open(csvfile, mode="w", newline='') as csvf:
            if list_objs is None or list_objs == []:
                csvf.write('[]')
            else:
                if cls.__name__ == 'Square':
                    attr = ["id", "size", "x", "y"]
                else:
                    attr = ["id", "width", "height", "x", "y"]
                doc = csv.DictWriter(csvf, fieldnames=attr)
                list_csv = []
                for inst in list_objs:
                    list_csv += [doc.writerow(inst.to_dictionary())]
