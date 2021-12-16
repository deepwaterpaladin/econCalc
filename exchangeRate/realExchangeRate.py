def realExchangeRate():
    Rn=float(input("Enter the nominal exchange rate: "))
    Pf=float(input("Enter the foreign price level: "))
    Pd=float(input("Enter the domestic price level: "))

    Rr= Rn*(Pf/Pd)

    print("The real exchange rate is", Rr)

realExchangeRate()