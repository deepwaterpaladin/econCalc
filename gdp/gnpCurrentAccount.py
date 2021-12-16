def gnp():
    C = int(input("Consumption Expenditures: "))
    I = int(input("Investment Expenditures: "))
    G = int(input("Government Expenditures on Goods and Services: "))
    CA = int(input("Current Account: "))

    GNP = (C+I+G+CA)
    print("Gross National Product is:", GNP)
gnp()