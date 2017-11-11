
print "*STORE ITEMS*"
print ""
print "doritos"
print "coffee"
print "coke"
print "pepsi"
print "pringles"
print "gum"
print "brownie"

doritos=1.00
coffee=2.00
coke=1.00
pepsi=1.00
pringles=0.50
gum=0.25
brownie=0.75

store=[doritos, coffee, coke, pepsi, pringles, gum, brownie]

print ""
order= input ("What is the order? ")
if order != doritos:
    if order != coffee:
        if order != coke:
            if order != pepsi:
                if order != pringles:
                    if order != gum:
                        if order != brownie:
                            input ("*ERROR* What is the order?")
quantity = input ("How many?")
total = order * quantity
print total
print ""

cash = input ("Change? *PLACE MONEY GIVEN* ")
print cash - total

