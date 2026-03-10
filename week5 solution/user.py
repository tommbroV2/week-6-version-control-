""" user.py
Contains the abstract User class and the classes that inherit from this (Lecturer and Student).
"""
from abc import ABC

class User(ABC):
    """
    Abstract User class
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def get_modules(self):
        return self.modules
    
#---------------

class Lecturer(User):
    """
    Lecturers are Users who teach modules within their subject areas.
    """
    def __init__(self, id, name):
        super().__init__(id, name)

        self.subject_areas = []

    def add_module(self, module):
        super().add_module(module)
        #Keep the module object updated with who the lecturers are.
        module.add_lecturer(self) 

#---------------

class Student(User):
    """
    Students are enrolled on any number of programmes and take modules.
    """
    def __init__(self, id, name):
        super().__init__(id, name)

        self.programmes = []        