""" Quick Documentation:
- This py file inlucdes functionality of inputting items, prices, and people.
- We crunch the numbers and divide the total between people. 
"""

""" Branch Backlog:
- Individual name as our <key>
- Create an object to correlate each item with specific individuals
- Create an object that has the running total of each individual
"""


from multiprocessing.sharedctypes import Value
from operator import truediv
# from __future__ import division
from datetime import datetime
import sys
import keyboard

class MinimumValueError(Exception): pass #handles: no inputs
class UnwantedStringError(Exception): pass #handles: bad strings in int inputs
class ErrorInput(Exception): pass #handles: bad inputs in strings

def namesInput(user_total):
    names_list = []
    while True:
        try:
            name_input = input("Enter a payer's name | Type 'DONE' to proceed: ")
            if name_input == "DONE":
                if len(names_list) == 0:
                    raise MinimumValueError
                break
            elif name_input == "" or name_input == " " or name_input.isdigit():
                raise ErrorInput

            names_list.append(name_input)
            user_total[name_input] = 0

        except MinimumValueError:
            print("Enter at least 1 name!")
        except ErrorInput:
            print("Enter a valid name")

    return names_list


def itemsInput(names_list, user_total):
    items_dict = {} #items dictionary with (key, value) as (name, price)

    while True:
        try:
            item_name = input("What is the item? | Type 'DONE' to proceed: ")
            if item_name == "DONE": 
                if len(items_dict) == 0: 
                    raise MinimumValueError
                break

            item_price = input(f"What is {item_name} price? ")
            items_dict[item_name] = float(item_price)
            divideToUser(item_name, items_dict, names_list, user_total)

        except ValueError:
            print("Enter a number for item price!")
        except MinimumValueError:
            print("Insert at least 1 item to continue!")

    return items_dict


def divideToUser(item: str, items_dict: dict, names: list, user_total: dict) -> list: #itemsList and namesList parameter
    print("\033[96m" + "WHO " + item + "?" + "\033[0m")
    
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")
    
    who_list = []
    number_of_people = len(names)
    
    while True:
        try: 
            name_string = input("Enter 0 for all | For specific people enter number seperated by white space: ")
            if name_string == "0":
                who_list = names
            else:
                for char in name_string:
                    if char.isdigit():
                        index = int(char)
                        who_list.append(names[index - 1])
                number_of_people = len(who_list)
                if number_of_people == 0:
                    raise UnwantedStringError
            break
        
        except UnwantedStringError:
            print("Please enter a number for name selection!")
    
    even_divison = items_dict[item] / number_of_people
    for j in range(number_of_people):
        user_total[who_list[j]] += even_divison #updates running total between everyone
        print(f"{who_list[j]} owes ${even_divison}!")

    return

# --- RUNS IN MAIN ---
def splitCheck():
    user_total = {}

    print("\033[96m" + "Welcome to Xplitter" + "\033[0m")
    
    title = input("Who is money owed to?:") + f"'s Payday on ({datetime.now()})"
    print(title)
    
    names_list = namesInput(user_total)
    items_dict = itemsInput(names_list, user_total)

    print(items_dict)
    print(user_total)