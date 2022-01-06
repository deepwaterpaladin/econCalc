def calcRateOfReturn():
    p = int(input("Enter the price at the beginning of the holding period: "))
    pt = int(input("Enter the price at the end of the holding period: "))
    c = int(input("Enter the sum of coupon/dividends made during the holding period: "))
    r = int(((pt - p + c)/p)*100)

    print(f"The rate of return is {r}%")

calcRateOfReturn()