# the financial account is the main record of financial flows between countries.

def financialAccount():
    acquisitions=int(input("Net acquisitions of financial assets: "))
    liabilities=int(input("Net incurrences of liabilities: "))
    derivatives=int(input("Net changes in financial derivatives: "))

    financialAccountBalance=int(acquisitions-liabilities+derivatives)

    print("Balance on Financial Account: ", financialAccountBalance)

financialAccount()