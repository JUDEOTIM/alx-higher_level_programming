#!/usr/bin/python3
""" Base Module
"""
from typing import Optional
import json
import csv
import turtle as t
# import tkinter as tk


class Base:

    """Base Class
    Attributes:
        id (int): id attr
    """

    __nb_objects = 0

    def __init__(self, id: Optional[int] = None) -> None:
        """ instance init function
        Args:
            id (Optional[int], optional): parsed id arg
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts dicts to json to the data
        Args:
            list_dictionaries (list): list of dicos
        Returns:
            json: dumped json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save json to file
        Args:
            list_objs (list): List of objects
        """
        filename = cls.__name__+".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ load from json string
        Args:
            json_string (dict strin): Description
        Returns:
            json: Retreived dict
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create new instance dictionary
        Args:
            **dictionary: dictionary
        Returns:
            dict: new instance dict
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(2, 3)
            else:
                new_instance = cls(2)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """ Load from file
        Returns:
            list: list of dict
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as file:
                dict_list = Base.from_json_string(file.read())
                return [cls.create(**item) for item in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save file to csv
        Args:
            list_objs (list): List of dicos
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                [writer.writerow(obj.to_dictionary()) for obj in list_objs]
                # for obj in list_objs:
                #     writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load from csv file
        Returns:
            list: List of new object diction instance
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(file, fieldnames=fieldnames)
                dict_list = [dict([k, int(v)] for k, v in d.items())
                             for d in dict_list]
                return [cls.create(**dic) for dic in dict_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws the shapes
        Args:
            list_rectangles (list): List of rectangle object
            list_squares (list): List of square object
        """
        turt = t.Turtle()
        turt.screen.bgcolor("black")
        turt.pensize(4)
        turt.shape("turtle")

        turt.color("yellow")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("blue")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()


