# record of transactions in goods, services, investment income, and unilateral transfers between the residents of a country and the rest of the world.

def calcCurrentAccount():
    gsExports=int(input("Goods and Services Exports: "))
    primaryIncome=int(input("Primary Income: "))
    secondaryIncome=int(input("Secondary Income: "))
    gsImports=int(input("Goods and Services Imports: "))
    piPayments=int(input("Primary Income Payments: "))
    siPayments=int(input("Secondary Income Payments: "))

    currentAccount=int(gsExports+primaryIncome+secondaryIncome-gsImports-piPayments-siPayments)

    print("Current Account is: ", currentAccount)

calcCurrentAccount()

# one thing I could do later is to shorten the variable names to make it easier to read.
