import fractions

def calculateFactorAbundance():
    countryA = input("Enter the name of the first country: ")
    countryB = input("Enter the name of the second country: ")
    countryACapital = int(input("Capital (K) for the first country: "))
    countryALabour = int(input("Labour (L) for the first country: "))
    countryBCapital = int(input("Capital (K) for the second country: "))
    countryBLabour = int(input("Labour (L) for the second country: "))

    factorAbundanceA = fractions.Fraction(numerator=countryACapital, denominator=countryALabour)
    factorAbundanceB = fractions.Fraction(numerator=countryBCapital, denominator=countryBLabour)
    
    print("the K/L ratio for", countryA, fractions.Fraction(numerator=countryACapital, denominator=countryALabour))
    print("the K/L ratio for", countryB, fractions.Fraction(numerator=countryBCapital, denominator=countryBLabour))
    
    if factorAbundanceA > factorAbundanceB:
        print(countryA, "is capital abundant, compaired to", countryB, "and", countryB, "is labour abundant, compared to", countryA)
    elif factorAbundanceB > factorAbundanceA:
        print(countryB, "is capital abundant, compaired to", countryA, "and", countryA, "is labour abundant, compared to", countryB)
    
    return factorAbundanceA, factorAbundanceB

calculateFactorAbundance()
