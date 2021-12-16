def gnp():
    C=int(input("Consumption Expenditures: "))
    S=int(input("Private Savings (households & firms): "))
    T=int(input("Net taxes (taxes paid minus transfer payments received): "))

    GNP=int(C+S+T)

    print("Gross National Product is:", GNP)
gnp()