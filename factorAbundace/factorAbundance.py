import random
import fractions

nationA= input("Enter the name of the first nation: ")
nationB= input("Enter the name of the second nation: ")

def factorAbundance(nationA, nationB):
    Ka=random.randint(1,100)
    La=random.randint(10,200)
    Kb=random.randint(1,100)
    Lb=random.randint(10,200)

    nationAFactorAbundance= fractions.Fraction(numerator=Ka,denominator=La)
    nationBFactorAbundance= fractions.Fraction(numerator=Kb,denominator=Lb)

    guessesTaken=0

    
    print(f"{nationA} has {Ka} machines and {La} workers", f"& {nationB} has {Kb} machines and {Lb} workers")

    capitalAbundantCan= nationAFactorAbundance>nationBFactorAbundance
    capitalAbundantUsa= nationBFactorAbundance>nationAFactorAbundance


    while guessesTaken < 3:
        guess=input("What country is capital abundant? ")
        guessesTaken=guessesTaken+1
        if guess == nationA and capitalAbundantCan==True:
                print("You are correct!")
                break
        elif guess == nationB and capitalAbundantUsa==True:
                print("You are correct!")
                break
        else:
            print("Incorrect. Guess Again")

factorAbundance(nationA, nationB)
