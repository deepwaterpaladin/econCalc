stock=input("ticker symbol: ")

def marketCap():
    stockPrice=float(input("Stock price: "))
    sharesOutstanding=float(input("Shares outstanding: "))
    marketCap=(int(stockPrice)*int(sharesOutstanding))

    print(f"The market cap of {stock} is {marketCap}")

marketCap()