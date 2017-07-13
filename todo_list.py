"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    print "The add_to_list function has not yet been written"
    return my_list

def view_list(my_list):
    """Print each item in the list."""

    print "The view_list function has not yet been written"


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
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
                
        

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

