def calcGDP():
    c = int(input("Private Consumption: "))
    i = int(input("Gross Investment: "))
    g = int(input("Government Investment: "))
    x = int(input("Net Export: "))
    m = int(input("Net Import: "))

    gdp = int(c+i+g+x-m)
    print(f"GDP: ${gdp}")

calcGDP()