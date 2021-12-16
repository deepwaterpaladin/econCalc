# this function can be used to determine which bond is more valuable in the future
# when taking into account exchange rates (spot and forward rates)

def bondCalc ():
    countryA = input("Enter the name of the first country: ")
    countryB = input("Enter the name of the second country: ")
    investment = float(input("Enter the investment: "))
    interestRateA = float(input("Enter the interest rate of the bond offered in the first country: "))
    interestRateB = float(input("Enter the interest rate of the bond offered in the second country: "))
    R = float(input("Enter the spot rate: "))
    F = float(input("Enter the forward rate: "))
    bondA = investment*interestRateA
    bondB = (F/R)*interestRateB*investment

    print("The future value of a bond offered in", countryA, "is", bondA, "and the future value of a bond offered in", countryB, "is", bondB)

    if bondA > bondB:
        print("The bond offered in", countryA, "is worth more in the future in terms of the home currency.")
    elif bondA < bondB:
        print("The bond offered in", countryB, "is worth more in the future in terms of the home currency.")
bondCalc()

