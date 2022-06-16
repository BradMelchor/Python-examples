#!/usr/bin/env python3
def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()
    
def list(inventory):
    i = 1
    for item in inventory:
        print(str(i) + ". " + item)
        i += 1
    print()
        
def add(inventory):
    item = input("Name: ")
    i = 1
    while i < 5:
        inventory.append(item)
        print(item + " was added.\n")
        break

def edit(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid number, please try again.")
    else:
        item = input("Update Name: ")
        inventory.pop(number-1)
        inventory.insert(number-1, item)
        print("Item number " + str(number) + " was updated.")
        print()

def delete(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid number, please try again.")
    else:
        item = inventory.pop(number-1)
        print(item + " was dropped.")
        print()
    
def main():
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    print("The Wizard Inventory Program")
    print()

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "show":
            list(inventory)
        elif command.lower() == "grab":
            if len(inventory) < 4:
                add(inventory)
            else:
                print("You can't carry any more items. Drop something first.")
                print()
        elif command.lower() == "edit":
            edit(inventory)
        elif command.lower() == "drop":
            delete(inventory)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. please try again")
            
if __name__ == "__main__":
    main()
