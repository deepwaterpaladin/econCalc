def calcGNP():
    c = input("Private Consumption: ")
    i = input("Gross Investment: ")
    g = input("Government Investment: ")
    x = input("Net Export: ")
    m = input("Net Import: ")
    npi = input("Net Primary Income: ")
    nsi = input("Net Secondary Income: ")
    gdp = (int(c)+int(i)+int(g)+int(x)-int(m))

    gnp = (gdp+int(npi)-int(nsi))
    
    print("GNP:", int(gnp))

calcGNP()