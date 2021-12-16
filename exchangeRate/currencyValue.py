def currencyChange():
    changeInValue = input("Did the currency appreciate or depreciate?: ")
    determinant = input("Was this in the long run, medium run, or short run?: ")
    longRunAppreciation = "Home goods are less expensive than foreign goods."
    mediumRunAppreciation = "Domestic economy grows slower than foreign economy."
    shortRunAppreciationA = "Interest rates rise at home and/or decline abroad."
    shortRunAppreciationB = "Expectations of future appreciation."
    longRunDepreciation = "Home goods are more expensive than foreign goods."
    mediumRunDepreciation = "Domestic economy grows faster than foreign economy."
    shortRunDepreciationA = "Interest rates fall at home and/or rise abroad"
    shortRunDepreciationB = "Expectations of future depreciation"

    if changeInValue == "appreciate":
        if determinant == "long run":
            print("In the long run, the value of", longRunAppreciation)
        elif determinant == "medium run":
            print("In the medium run, the value of", mediumRunAppreciation)
        elif determinant == "short run":
            print("In the short run, the value of", shortRunAppreciationA, "or", shortRunAppreciationB)
    elif changeInValue == "depreciate":
        if determinant == "long run":
            print("In the long run, the value of", longRunDepreciation)
        elif determinant == "medium run":
            print("In the medium run, the value of", mediumRunDepreciation)
        elif determinant == "short run":
            print("In the short run, the value of", shortRunDepreciationA, "or", shortRunDepreciationB)
currencyChange()