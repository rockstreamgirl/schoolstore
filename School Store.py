run = True
while run:
    total = 0.0
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
    print ""
    end = False
    while end == False:
        name = raw_input('What is the order (enter "end" when done)? ')
        if name == 'end':
            end = True
        elif name not in products:
            print ('*ERROR* Not a valid product ')
        else:
            price = products[name]
            done = False
            while done == False:
                try:
                    quantity = int(raw_input("How many? "))
                except ValueError:
                    print ("*ERROR* Quantity must be an integer")
                else:
                    done = True
                    
            total += price * quantity

    print total
    print ""

    cash = input ("Change? *PLACE MONEY GIVEN* ")
    print cash - total
    print ""
    print ""
