""" main.py
Code to test out the classes we have created for workshop 5.
"""
from datetime import date
import resource, module, user

if __name__ == '__main__':
    # create a module
    cmp1138 = module.Module("CMP1138", "Foundations of Programming")

    # create some users:
    lecture = user.Lecturer(1, "Wenting")
    lecture.add_module(cmp1138)
    student = user.Student(1, "Ambrose")
    student.add_module(cmp1138)

    # add a book to the module
    authors = ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"]
    book = resource.PrintedBook(authors, "Design Patterns", 1994, "United States", "Pearson Education")
    print(book.get_reference())
    cmp1138.add_item_to_reading_list( module.ReadingListItem(book, True) )

    # add a website to the module
    web_authors = ["w3shools"]
    web = resource.Website(web_authors, "Python Tutorial", 2026, "https://www.w3schools.com/python/", date(2026, 2, 14))
    cmp1138.add_item_to_reading_list( module.ReadingListItem(web, True) )

    # print the reading list
    cmp1138.print_reading_list()