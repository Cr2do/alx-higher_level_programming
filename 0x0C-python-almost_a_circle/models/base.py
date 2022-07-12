#!/usr/bin/python3
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id == None:
            self.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = self.__nb_objects
