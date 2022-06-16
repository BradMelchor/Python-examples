#!/usr/bin/env python3

def valid_int(prompt, low, high):
    while True:
        number= int(input(prompt))
        if number >= low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "And less than or equal to", high)
def calc_factors(prompt):
    factors = 0
    for x in range (1, prompt + 1):
        if prompt % x ==0:
            print(x)
            factors += 1

    return factors

def main():
    choice = "y"
    while choice.lower() == "y":

            print("Prime Number Checker")
            print()

            #get input from user
            is_prime= valid_int("Please enter an integer between 1 and 5,000: ", 1, 5000)
       
            if (is_prime % 2 == 1):
                print("The factors of your number are:" )
               #calculate factors
                factors = calc_factors(is_prime) 
                print(str(is_prime) +" " + "is a prime number.")
        
                #continue?
                choice = input("Continue? (y/n): ")
                print()
            else:
                print("The factors of your number are:" )
                #calculate factors
                factors = calc_factors(is_prime)
                print(str(is_prime) +" " + "is NOT a prime number.")
                print("It has " + str(factors) + " factors")
        
                #continue?
                choice = input("Continue? (y/n): ")
                print()
            

if __name__ == "__main__":
    main()
