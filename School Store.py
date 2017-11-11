
print "*STORE ITEMS*"
print ""
 
products = {
    'doritos': 1.00,
    'coffee': 2.00,
    'coke': 1.00,
    'pepsi':1.00,
    'pringles': 0.50,
    'gum': 0.25,
    'brownie': 0.75
    }

for name in products:
    print name

name = raw_input('What is the order?')
if name not in products:
    name = raw_input ('*ERROR* What is the order?')
price = products[name]
                       
quantity = input ("How many?")
total = price * quantity
print total
print ""

cash = input ("Change? *PLACE MONEY GIVEN* ")
print cash - total

