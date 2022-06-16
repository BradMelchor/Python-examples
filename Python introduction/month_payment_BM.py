#!/usr/bin/env python3

from decimal import Decimal
import locale as lc

def get_month_payment(loan_amount, yearly_interest_rate, years):
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    monthly_payment = Decimal("0.00")
    month_payment = loan_amount * monthly_interest_rate / (1 -1 / (1 + monthly_interest_rate) ** months)
    month_payment = month_payment.quantize(Decimal("1.00"))
    return month_payment
    

def main():
    print("Monthly Payment Calculator")
    print()
    print("DATA ENTRY")
    choice = "y"
    while choice.lower() == "y":
        loan_amount = Decimal(input("Loan Amount:          "))
        yearly_interest_rate = Decimal(input("Yearly interest rate: "))
        years = int(input("Years:                "))
        month_payment = get_month_payment(loan_amount, yearly_interest_rate, years)
        print()

        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        line = "{:20} {:>10}"
        line2 = "{:20} {:>10%}"
        line3 = "{:20} {:>11}"
        print("FORMATTED RESULTS")
        print(line.format("Loan amount:", lc.currency(loan_amount, grouping=True)))
        yearly_interest_rate = (yearly_interest_rate / 100)
        print(line2.format("Yearly interest rate:", yearly_interest_rate))
        print(line3.format("Number of years:", years))
        print(line3.format("Monthly Payment:", lc.currency(month_payment, grouping=True)), "\n")

        choice= input("Continue? (y/n): ")

if __name__ == "__main__":
    main()
