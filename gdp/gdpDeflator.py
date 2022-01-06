def gdpDeflator():
    nominalGDP = input("Nominal GDP: ")
    realGDP = input("Real GDP: ")
    deflator = ((int(nominalGDP)/int(realGDP))* 100)
    print(f"GDP deflator is: {deflator}")

gdpDeflator()