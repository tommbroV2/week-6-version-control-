""" Some basic python tests. Used for looking at how to use github Actions"""
import resource

def test_basics():
    assert 2 == 1+1
 
def test_printbook_reference(): 
    authors = ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"]
    book = resource.PrintedBook(authors, "Design Patterns", 1994, "United States", "Pearson Education")    
    reference = book.get_reference().replace("PrintedBook: ", "")

    assert reference == "Gamma,r., Helm,i., Johnson,a. and Vlissides,o. (1994) Design Patterns. United States:Pearson Education"