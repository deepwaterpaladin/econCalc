import fractions

def calculateFactorAbundance():
    countryA = input("Enter the name of the first country: ")
    countryB = input("Enter the name of the second country: ")
    countryACapital = int(input(f"Capital (K) for {countryA}: "))
    countryALabour = int(input(f"Labour (L) for {countryA}: "))
    countryBCapital = int(input(f"Capital (K) for {countryB}: "))
    countryBLabour = int(input(f"Labour (L) for the {countryB}: "))

    factorAbundanceA = fractions.Fraction(numerator=countryACapital, denominator=countryALabour)
    factorAbundanceB = fractions.Fraction(numerator=countryBCapital, denominator=countryBLabour)
    
    
    print(f"the K/L ratio for {countryA} is {fractions.Fraction(numerator=countryACapital, denominator=countryALabour)}")
    print(f"the K/L ratio for {countryB} is {fractions.Fraction(numerator=countryBCapital, denominator=countryBLabour)}")
    
    if factorAbundanceA > factorAbundanceB:
        print(f"{countryA} is capital abundant, compaired to {countryB} and {countryB} is labour abundant, compared to {countryA}")
    elif factorAbundanceB > factorAbundanceA:
        print(f"{countryB} is capital abundant, compaired to {countryA} and {countryA} is labour abundant, compared to {countryB}")
    return factorAbundanceA, factorAbundanceB

calculateFactorAbundance()
