"""resource.py
Contains the different Resource classes: PrintedBook, Website and Software
"""
from abc import ABC, abstractmethod

class Resource(ABC):
    """
    A referenceable Resource. 
    """
    def __init__(self, authors, title, publication_year, place_of_publication=None, publisher=None):
        self.authors = authors
        self.title = title
        self.publication_year = publication_year
        self.place_of_publication = place_of_publication
        self.publisher = publisher

    @abstractmethod
    def get_reference(self):
        """ Returns a string containing a harvard formatted reference """
        return (f"{self.author_reference_string()} ({self.publication_year}) {self.title}. {self.publication_place_str()}")

    def author_reference_string(self):
        # Creates a string containing the author names
        ref = ""
        # by using zip we can iterate two lists at the same time -- the list of authors and the index of the author
        for author, i in zip(self.authors, range(len(self.authors))):
            # add the authors last name to the reference
            ref += author.split()[-1] + ","
            # add the authors initials 
            for names in author.split()[:-1]:
                ref += names[1] + "."
            # Authors are separated by commas; the last two a separated by "and"
            if i == (len(self.authors)-2): # second to last
                ref += " and "
            elif i <= (len(self.authors)-3):
                ref += ", "

        return ref

    def publication_place_str(self):       
        publisher_str = ""
        # add place of publication
        if self.place_of_publication:
            publisher_str += self.place_of_publication + ":"
        # add publisher
        if self.publisher:
            publisher_str += self.publisher            
        return publisher_str

    def __str__(self):
        return self.get_reference()

#--------- 

class PrintedBook(Resource):
    """
    Class for referencing printed books
    """
    def __init__(self, authors, title, publication_year, place_of_publication=None, publisher=None, edition_number=None):
        super().__init__(authors, title, publication_year, place_of_publication, publisher)
        self.edition_number = edition_number

    def get_reference(self):
        if self.edition_number:            
            return (f"{self.author_reference_string()} ({self.publication_year}) {self.title}. {self.edition_number} Edition. {self.publication_place_str()}")
        else:
            super_ref = super().get_reference()
            return (f"PrintedBook: {super_ref}")

#--------- 

class Website(Resource):
    """
    Class for referencing websites
    """
    def __init__(self, authors, title, publication_year, web_address, date_accessed, place_of_publication = None, publisher = None):
        super().__init__(authors, title, publication_year, place_of_publication, publisher)
        self.web_address = web_address
        self.date_accessed = date_accessed


    def get_reference(self):
        super_ref = super().get_reference()
        datestr = self.date_accessed.strftime("%d %B %Y")
        return (f"PrintedBook: {super_ref} Available from {self.web_address} [accessed {datestr}]")
        
#--------- 

class Software(Resource):
    """
    Class for referencing software
    """

    def __init__(self, authors, title, publication_year, web_address, date_accessed, place_of_publication = None, publisher = None, version_number = None):
        super().__init__(authors, title, publication_year, place_of_publication, publisher)
        self.version_number = version_number
        self.web_address = web_address
        self.date_accessed = date_accessed


    def get_reference(self):
        if self.version_number:            
            ref = (f"{self.author_reference_string()} ({self.publication_year}) {self.title}. version {self.version_number} {self.publication_place_str()}")
        else:
            ref = super().get_reference()
        datestr = self.date_accessed.strftime("%d %B %Y")
        return (f"PrintedBook: {ref} Available from {self.web_address} [accessed {datestr}]")
        

