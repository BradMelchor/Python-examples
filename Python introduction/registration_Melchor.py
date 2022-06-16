#!/usr/bin/env python3

#display message
print("Student Registration")
print()

#input from user
first_name= input("First name:\t")
last_name= input("Last name:\t")
birth_year= input("Birth year:\t")

#calculate name and temporary password
name= first_name + " " + last_name
temp_pass= first_name + "*" + birth_year

#display results
print("Welcome " + name+ "!")
print("Your registration is complete.")
print("Your temporary password is: " + temp_pass)
