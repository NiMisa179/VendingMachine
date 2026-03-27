from decimal import Decimal

vendM = ["water", "chips Mini", "chips Mid", "chips Maxi", "coca Cola",
         "fanta Lemonade", "fanta Orange", "soda", "coca Cola Light", "pepsi",
         "pepsi Max", "chocolate", "chocolate strawberry", "mini chocolate", "choco"
         ]

prices = [0.5, 0.7, 1.2, 2, 1,
          1, 1, 1, 1.2, 1.3,
          1.5, 1.7, 1.8, 0.2, 0.5]

print("----------------------------")
for i in range(len(vendM)):
    print(f"{i+1:<3}{vendM[i]:<22}{prices[i]:<10}")
print("----------------------------")

print("IT WORKs!!!!!!!")

pId = int(input("Type the product 's ID: "))

price = prices[pId - 1]
print("You choose", vendM[pId - 1], ". It costs", price)
cash = eval(input("Type cash: "))

change = Decimal(Decimal(str(cash)) - Decimal(str(price))) * 100
change = abs(change)

dievra = change // 200
monoevra = (change % 200) // 100
misoevra = ((change % 200) % 100) // 50
dekalepta = (((change % 200) % 100) % 50) // 10

print("\n", dievra, ":2\u20ac \n", monoevra, ":1\u20ac \n", misoevra, ":0,5\u20ac \n", dekalepta, ":0,1\u20ac")
