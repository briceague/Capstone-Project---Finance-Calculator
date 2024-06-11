#code for different types of finance calculators

import math

#different types of calculations 
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#asking the user what type of calculation they want
type_of_calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed ")

#code to ensure the entered answer isn't case sensitive
option_1 = 'investment'
option_2 = 'bond'

#If statement run when variations of investment is typed
if type_of_calculation.upper() == option_1.upper():

    #checking the amount of money the person is deposting 
    amount_of_money_depositing = float(input("How much money are you depositing in rands? "))

    #the rate at which they're investing 
    interest_rate = float(input("What is the interest rate? "))

    #the amount of years they're investing for
    years_investing = float(input("How many years would you like to invest for? "))

    #asking if they want simple or compound interest
    interest = input("Do you want simple or compound interest? ")

    #variables to ensure entered answers aren't case sensitive
    interest_compound = 'compound'
    interest_simple = 'simple'

    #if statement for if simple  is entered
    if interest.upper() == interest_simple.upper():
        value_after_investing = amount_of_money_depositing*(1 + ((interest_rate/100)*years_investing))
        print("Your amount after investing for", years_investing, "is R", value_after_investing )
    
    #elif statement for if compound is entered
    elif interest.upper() == interest_compound.upper():
        value_after_investing = amount_of_money_depositing*(1 + ((interest_rate/100)**years_investing))
        print("Your amount after investing for", years_investing, "is R", value_after_investing )

    else:
        print("You have not entered an acceptable answer")

#If statement run when variations of investment is typed
elif type_of_calculation.upper() == option_2.upper():

    present_value_of_house = float(input("What is the present value of the house in rands? "))

    #the rate at which they're investing 
    interest_rate = ((float(input("What is the interest rate? ")))/100)/12

    #amount of months they're planning to take to repay the bond
    number_of_months_for_repayment = float(input("How many months do you plan to take to repay the bond? "))

    #the total amount a person will need to pay
    repayment = round((interest_rate * present_value_of_house)/(1 - (1 + interest_rate)**(-number_of_months_for_repayment)))

    print("Your total repayment is R",repayment)

else:
    print("You have not entered accurate data")