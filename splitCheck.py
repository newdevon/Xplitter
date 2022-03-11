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
import sys
import keyboard

def namesInput():
    name_input = input("Enter a name: ")
    # while True:
        # name_input = input("Enter a name: ")
    #     if keyboard.is_pressed('q'):  # if key 'q' is pressed 
    #             print('You Pressed A Key!')
    #             break  # finishing the loop

    

def itemsInput():
    names_list = ["Steven", "Joanne", "Jay", "Xuejin", "Sharon"]

    items_dict = {} #items dictionary with (key, value) as (name, price)

    while True:
        item_name = input("What is the item? | Type 'DONE' to proceed: ")
        if item_name == "DONE":
            break
        else: #need to write cases for invalid inputs like non-intger values
            item_price = input(f"What is {item_name} price? ")
            items_dict[item_name] = int(item_price)
            divideToUser(item_name, items_dict, names_list)
        
    return items_dict

#Can declare parameter and return types in Python for documentation
def divideToUser(item: str, items_dict: dict, names: list) -> list: #itemsList and namesList parameter
    print("\033[96m" + "WHO " + item + "?" + "\033[0m")
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")
    
    name_string = input("Enter 0 for all | For specific people enter number seperated by white space: ")
    if name_string == "0":
        print("Dividing evenly to every person! Waiting for implementation...")
    else:    
        who_list = list(map(int, name_string.split())) #list of string converted to integers 
 
    even_divison = int(items_dict[item] / len(who_list))
    
    for j in range(len(who_list)):
        print(f"{names[who_list[j]-1]} owes ${even_divison}!")
    return even_divison

def splitCheck():

    print("\033[96m" + "Welcome to Xplitter" + "\033[0m")
    
    title = input("Enter file title:")
    print(title)
    
    # namesInput()

    items_dict = itemsInput()
    print(items_dict)
