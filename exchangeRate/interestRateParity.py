def interestRateParity():
    homeA = input("Enter the name of the home country: ")
    foreignB = input("Enter the name of the foreign country: ")
    interestRateA = float(input("Enter the interest rate of the first country: "))
    interestRateB = float(input("Enter the interest rate of the second country: "))
    investmentA = float(input("Enter the potential investment of the first country: "))
    investmentB = float(input("Enter the potential investment of the second country: "))
    R = float(input("Enter the spot rate: "))
    F = float(input("Enter the forward rate: "))

    interestRateParity= (F-R)/R
    print("The interest rate parity exchange rate is", interestRateParity)

    if interestRateParity > 0:
        print("The", homeA, "is more likely to experience currency depreciation, and i>i*")
    elif interestRateParity < 0:
        print("The", homeA, "is more likely to experience currency appreciation, and i<i*")

interestRateParity()