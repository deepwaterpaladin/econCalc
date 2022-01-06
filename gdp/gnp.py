def calcGNP():
    c = int(input("Private Consumption: "))
    i = int(input("Gross Investment: "))
    g = int(input("Government Investment: "))
    x = int(input("Net Export: "))
    m = int(input("Net Import: "))
    npi = int(input("Net Primary Income: "))
    nsi = int(input("Net Secondary Income: "))
    
    gdp = int(c+i+g+x-m)
    gnp = int(gdp+npi-nsi)
    
    print(f"GNP: {gnp}")

calcGNP()