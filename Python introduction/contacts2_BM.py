#!/usr/bin/env python3
import csv
import sys

FILENAME = "contacts.csv"
def exit_program():
    print("Terminatiing program.")
    sys.exit()
    
def write_contacts(contacts):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
    except OSError as e:
            print(type(e), e)
            exit_program()
    except Exception as e:
            print(type(e), e)
            exit_program()
def read_contacts():
    try:
        contacts  = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    except FileNotFoundError as e:
        print("Could not find contacts file!")
        print("Starting new contacts file...")
        print()
        return contacts
    except Exception as e:
        print(type(e), e)
        exit_program()
        
def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("exit - Exit program")
    print()
def list_contacts(contacts):
    for i in range(0, len(contacts)):
        contact= contacts[i]
        print(str(i+1) + ". " + contact[0])
def view_contacts(contacts):
    while True:
        try:
            view = int(input("Number: "))
        except ValueError:
            print("Invalid Integer.")
            continue
        if view < 1 or view > len(contacts):
            print("Invalid contact number.")
        else:
            contact = contacts[view - 1]
            print("Name: " + contact[0])
            print("Email: "+ contact[1])
            print("Phone: "+ contact[2])
            break
def add_contacts(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact1 = []
    contact1.append(name)
    contact1.append(email)
    contact1.append(phone)
    contacts.append(contact1)
    write_contacts(contacts)
    print(name + " was added.\n")
def delete_contacts(contacts):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid Integer.")
            continue
        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
        else:
            contact = contacts.pop(number - 1)
            write_contacts(contacts)
            print(contact[0] + " was deleted.\n")
            break
    
def main():
    contacts = read_contacts()
    print("Contact Manager")
    print()
    
    display_menu()
    
    while True:
        command = input("Command : ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "view":
            view_contacts(contacts)
        elif command.lower() == "add":
            add_contacts(contacts)
        elif command.lower() == "del":
            delete_contacts(contacts)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
