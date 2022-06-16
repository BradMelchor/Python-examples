#!/usr/bin/env python3

#display hello message
print("Change Calculator")


#get dollar amount
quarter = .25
dime = .10
nickel = .05
penny = .01




choice = "y"
while choice.lower()== "y":
    print()
    total_money= float(input("Enter dollar amount (for example, .56, 7.85): "))
    print()
    minusq = int(total_money / quarter)
    new_total = total_money - (minusq * quarter)
    
    minusd= int(new_total / dime)
    new_total2 = new_total - (minusd * dime)
    
    minusn= int(new_total2 / nickel)
    new_total3 = new_total2 - (minusn * nickel)
    
    minusp = int(new_total3 / penny)
    new_total4 = new_total3 - (minusp * penny)
    
    print("Quarters:",minusq)
    print("Dimes:   ", minusd)
    print("Nickels: ", minusn)
    print("Pennies: ", minusp)
    print()
    choice = input("Continue (y/n)?: ")
    

if choice != "n" and "y":
    print("please enter y or n")
    choice = input("Continue (y/n)?: ")

print()
print("Bye!")




