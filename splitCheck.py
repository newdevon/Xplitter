""" Quick Documentation:
- This py file inlucdes functionality of inputting items, prices, and people.
- We crunch the numbers and divide the total between people. 
"""

""" Branch Backlog:
- Individual name as our <key>
- Create an object to correlate each item with specific individuals
- Create an object that has the running total of each individual
"""


from operator import truediv
# from __future__ import division
import sys
import keyboard

def namesInput():
    names_list = []
    while True:
        name_input = input("Enter a payer's name | Type 'DONE' to proceed: ")
        if name_input == "DONE": break
        else: names_list.append(name_input)

    return names_list
    

def itemsInput(names_list):

    items_dict = {} #items dictionary with (key, value) as (name, price)

    while True:
        item_name = input("What is the item? | Type 'DONE' to proceed: ")
        if item_name == "DONE": break
        else: #need to write cases for invalid inputs like non-intger values
            item_price = input(f"What is {item_name} price? ")
            items_dict[item_name] = float(item_price)
            print(items_dict)
            divideToUser(item_name, items_dict, names_list)
        
    return items_dict

#Can declare parameter and return types in Python for documentation
def divideToUser(item: str, items_dict: dict, names: list) -> list: #itemsList and namesList parameter
    print("\033[96m" + "WHO " + item + "?" + "\033[0m")
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")
    
    who_list = []
    number_of_people = len(names)

    name_string = input("Enter 0 for all | For specific people enter number seperated by white space: ")
    if name_string == "0":
        who_list = names
    else:
        for char in name_string:
            if char.isdigit():
                index = int(char)
                who_list.append(names[index - 1])
        number_of_people = len(who_list)
 
    even_divison = items_dict[item] / number_of_people
    
    for j in range(number_of_people):
        print(f"{who_list[j]} owes ${even_divison}!")
    return even_divison

def splitCheck():

    print("\033[96m" + "Welcome to Xplitter" + "\033[0m")
    
    title = input("Enter file title:")
    print(title)
    
    names_list = namesInput()
    items_dict = itemsInput(names_list)

    print(items_dict)
