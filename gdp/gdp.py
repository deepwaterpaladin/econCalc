def calcGDP():
    c = input("Private Consumption: ")
    i = input("Gross Investment: ")
    g = input("Government Investment: ")
    x = input("Net Export: ")
    m = input("Net Import: ")

    gdp = (int(c)+int(i)+int(g)+int(x)-int(m))

    print("GDP:", int(gdp))

calcGDP()