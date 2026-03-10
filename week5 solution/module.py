"""module.py
Contains the Module class and the ReadingListItem class
"""

class Module:
    """
    Modules are taken by Students and taught by Lecturers.
    """
    def __init__(self, code, name):
        self.code = code
        self.name = name

        self.reading_list = []
        self.lectures = []

    def add_item_to_reading_list(self, item):
        self.reading_list.append(item)

    def add_lecturer(self, lecturer):
        self.lectures.append(lecturer)

    def print_reading_list(self):
        print (f"Reading list for {self.code} {self.name}:")
        for item in self.reading_list:
            print(item)

#--------------

class ReadingListItem:
    """
    Modules have reading lists containing essential and recommended items/resources. 
    """
    def __init__(self, resource, is_essential):
        self.resource = resource
        self.is_essential = is_essential

    def __str__(self):
        if self.is_essential:
            return str(self.resource) + " [essential]"
        else:
            return str(self.resource) + " [recommended]"