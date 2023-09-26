##
##  Lab 05 - Pizza Order
##
##  Andrew Aberer | aaberer@colostate.edu

# STEP 1
def get_topping_one(pizza_order):
    return pizza_order[0:6]


# STEP 2
def get_topping_two(pizza_order):
    return pizza_order[8:17]


# STEP 3
def get_price(pizza_order):
    price = str(pizza_order[19:22])
    dec = int(price, 16)
    return dec


# STEP 4
def too_much_cheese(pizza_order):
    if pizza_order[0:6] == 'cheese':
        return True
    else:
        return False


# STEP 5
def full_order(pizza_order):
    output = ''
    if too_much_cheese(pizza_order) == True:
        output += 'That\'s a lot of cheese'
    if too_much_cheese(pizza_order) == False and get_price(pizza_order) == 45:
        output += 'Wow that\'s an expensive pizza!'
    if pizza_order[8:17] == 'pineapple':
        output += 'Pineapple DOES belong on pizza.'
    elif pizza_order[8:17] == 'artichoke':
        output += 'That\'s an interesting combo.'
    elif get_price(pizza_order) < 13 or get_price(pizza_order) >= 50:
        output += 'Are we sure they\'re charging us right?'
    else:
        output = 'Now that\'s a smokin\' deal! Give me more!'
    return output


def run():
    print(get_topping_one("cheese, pepperoni, FF"))
    print(get_topping_one("olives, pepperoni, FF"))
    print(get_topping_two("cheese, pepperoni, FF"))
    print(get_topping_two("olives, pepperoni, FF"))
    print(get_price("cheese, pepperoni, FF"))
    print(get_price("olives, pepperoni, FF"))
    print(too_much_cheese("cheese, pepperoni, FF"))
    print(too_much_cheese("olives, pepperoni, FF"))
    print(full_order('onions, pineapple, 11'))
    #create your own tests here
    return # make sure this line is last

if __name__ == "__main__":
    run()
    