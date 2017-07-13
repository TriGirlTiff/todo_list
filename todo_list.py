"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    add_item = raw_input("What would you like to add? ")
    item_position = int(raw_input("Where do you want to put it? "))
    item_position = item_position -1

    my_list.insert(item_position,add_item)

    return my_list

def view_list(my_list):
    """Print each item in the list."""

    index = 0
    while len(my_list)> index:
        print index, my_list[index]
        index += 1

def delete_item(my_list):
    del my_list[0]
    return my_list





def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    D. Delete first item
    >>> """

    user_continuing = True
    while user_continuing:
        user_choice = raw_input(user_options)
        user_choice = user_choice.upper()

        if user_choice == "A":
            my_list = add_to_list(my_list)
        elif user_choice == "B":
            view_list(my_list)
        elif user_choice == "C":
            user_continuing = False 
        elif user_choice == "D":
            my_list = delete_item(my_list)

        else:
            print "Please enter a valid letter"

        

#-------------------------------------------------

a_list = []
display_main_menu(a_list)

