def exchangeRateFactor():
    determinant = input("Enter the determinant of the exchange rate factor: ")
    longRun = "Purchasing power parity"
    mediumRun = "the business cycle."
    shortRunA = "Interest Parity"
    shortRunB = "Speculation"

    if determinant == "long run":
        print("In the long run, the exchange rate depends on", longRun)
    elif determinant == "medium run":
        print("In the medium run, the exchange rate depends on", mediumRun)
    else:
        if determinant == "short run":
            print("In the short run, the exchange rate depends on either the", shortRunA, "or", shortRunB)
    
    return longRun, mediumRun, shortRunA, shortRunB, determinant
exchangeRateFactor()
