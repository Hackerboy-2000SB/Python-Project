""" -> datastructure - Fullname - Phonenumber - Email

-> Add a new item to phone
-> List items from book
-> Remove item from book
-> Search items from book
-> Store book data to a file
-> Reload data when we start phone

Notes:

cmd prompt => window
terminal => linux/osx

$ pip install requests

=> Added Date
=> Sort by date
=> Sort by Name
"""

##import csv
import os
from csv import DictReader, DictWriter

filename = "phonebook_python.csv"


def add_item(phonebook, *, name, number, email):
    bookitem = {"fullname": "", "number": "", "email": ""}
    # item = bookitem.copy()
    bookitem["fullname"] = name
    bookitem["number"] = number
    bookitem["email"] = email
    phonebook.append(bookitem)


def search_item(phonebook, keyword):
    for index, item in enumerate(phonebook):
        if keyword in item["fullname"]:
            print("Found: {}/{}/{} Index: {}".format(
                item["fullname"], item["number"], item["email"], index
            ))

def is_duplicate(phonebook):
    """ this function should return True if email is already present in phonebook
    and return False if email is not present
    """
    pass


def list_items(phonebook):
    print("FullName\t PhoneNumber\t Email\n==========", end="\n")
    for item in phonebook:
        print("{}\t {}\t {}".format(
            item["fullname"], item["number"], item["email"]
        ))
    print("=" * 10)


def add_action():
    """ validate all empty fields """
    items = []
    while True:
        fullname = input("Enter Name: ")
        if not fullname.strip():
            print("Fullname cannot be empty. Please continue")
            continue
        ph_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        items.append((fullname, ph_number, email))
        char = input("Do you want to continue? [y/yes]: ")
        if not (char.lower() == "y" or char.lower() == "yes"):
            break
    return items

# default argument
def write_to_csv(phonebook, filename, write_mode = "w"):
    with open(filename, write_mode) as csvfile:
        writer = DictWriter(csvfile, fieldnames=["fullname", "number", "email"])
        writer.writeheader()
        for each in phonebook:
            writer.writerow(each)


def cli():
    global filename
    phonebook = []
    if os.path.exists(filename):
        with open(filename, "r") as csvfile:
            reader = DictReader(csvfile, fieldnames=["fullname", "number", "email"])
            next(reader)
            phonebook.extend(reader)
    while True:
        print("""
        A: Add
        L: List
        S: Search
        R: Remove
        E: Exit
        """)
        action = input("Please select a action: ")
        if action.upper() == "A":
            collected_items = add_action()
            for name, number, email in collected_items:
                add_item(phonebook, name=name, email=email, number=number)
        elif action.upper() == "L":
            # list action
            list_items(phonebook)
        elif action.upper() == "S":
            # search action
            keyword = input("Enter a keyword to search: ")
            search_item(phonebook, keyword)
        elif action.upper() == "R":
            # remove action
            """ task """
            pass
        elif action.upper() == "E":
            write_to_csv(phonebook, filename)
            break
        else:
            print("invalid action selected")


# print(__name__)
if __name__ == "__main__":
    cli()
