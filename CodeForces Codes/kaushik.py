from abc import ABCMeta, abstractclassmethod

class Student:
    __name = None
    __age = None
    def __init__(self, name, age, id):
        self.__name = name
        self.__age = age
        self.__id = id
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def display(self):
        print(self.__name, self.get_name(), self.__age, self.get_id())
st_obj = Student("Tom", 20, 9)
st_obj.display()
