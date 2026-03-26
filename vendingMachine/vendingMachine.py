from decimal import Decimal

price = eval(input("Type the price of the product: "))
cash = eval(input("Type cash: "))

change = Decimal(Decimal(str(cash)) - Decimal(str(price))) * 100
change = abs(change)

dievra = change // 200
monoevra = (change % 200) // 100
misoevra = ((change % 200) % 100) // 50
dekalepta = (((change % 200) % 100) % 50) // 10

print("\n", dievra, ":2\u20ac \n", monoevra, ":1\u20ac \n", misoevra, ":0,5\u20ac \n", dekalepta, ":0,1\u20ac \n")
