# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497
order1 = ('manan', 'holyoke', '', 'chicken', 'brown', 'pinto', True, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream', 'guacamole')

def get_protein(choice: tuple) -> tuple:
    price = 0.0
    for item in choice:
        if item == 'chicken' or item == 'veggies':
            price += 2.5
        elif item == 'steak' or item == 'barbacoa':
            price += 3.5
        elif item == 'carnitas':
            price += 3.0
        elif item in ('', ' '):
            price += 0
    return price
# print(get_protein(order1))
def get_rice(choice: tuple) -> tuple:
    price = 0
    for item in choice:
        if item == 'white':
            price += 2.5
        elif item == 'brown':
            price += 3.5
        elif item == '' or item == ' ':
            price += 0
    return price
# print(get_rice(order1))
def get_beans(choice: tuple) -> tuple:
    price = 0
    for item in choice:
        if item == 'black' or item == 'pinto':
            price += 2.5
        elif item == '' or item == ' ':
            price += 0
    return price
# print(get_beans(order1))
def get_burrito(choice):
    if choice:
        return 2
    else:
        return 0
# print(get_burrito(order1))
def get_toppings(choice: tuple) -> tuple:
    toppings_prices = {'guacamole' : 2.75, 'tomato salsa': 2.5, 'chili corn salsa': 1.75, 'tomatillo green chili salsa': 2.0, 'sour cream': 2.5, 'fajita veggies': 2.5, 'cheese': 2.0, 'queso blanco': 2.75, '': 0, ' ': 0}
    veggiestrue = 'veggies' in choice

    price = 0
    for item in choice:
        if item in toppings_prices:
            if veggiestrue and item in ('guacamole', 'fajita veggies'):
                continue
            price += toppings_prices[item]
    return price
# print(get_toppings(order1))
def apply_discount(choice, price):
    percentdiscount = {'MAGIC': 0.05, 'SUNDAYFUNDAY': .10}
    flatdiscount = {'FLAT3': 3.0, '': 0, ' ': 0}
    for item in choice:
        if item in percentdiscount:
            price -= price * percentdiscount[item]
        elif item in flatdiscount:
            price -= flatdiscount[item]
    return price
# print(apply_discount(order1))
def approximate_time(choice):
    delivery_times = {'amherst': 15, 'north amherst': 15, 'south amherst': 15, 'hadley': 15, 'northampton': 30, 'south hadley': 30, 'belchertown': 30, 'sunderland': 30, 'holyoke': 45, 'greenfield': 45, 'deerfield': 45, 'springfield': 45,}
    location = choice[1]  
    
    if location in delivery_times:
        return delivery_times[location]
    else:
        return "Location not found"
# print(approximate_time(order1))
def generate_invoice(choice):
    customer_name = choice[0]
    location = choice[1]
    discount = choice[2]
    protein = choice[3]
    rice = choice[4]
    beans = choice[5]
    burrito = choice[6]
    toppings = choice[7:]

    pprice = get_protein(protein)
    rprice = get_rice(rice)
    bprice = get_beans(beans)
    burprice = get_burrito(burrito)
    topprice = get_toppings(toppings)

    subtot = pprice + rprice + bprice + burprice + topprice
    flatdiscount = {'FLAT3': 3.0, '': 0, ' ': 0}
    percentdiscount = {'MAGIC': 0.05, 'SUNDAYFUNDAY': 0.10}

    if discount in percentdiscount:
        total_price = subtot * (1 - percentdiscount[discount])
        money_saved = subtot * percentdiscount[discount]
    elif discount in flatdiscount:
        total_price = subtot - flatdiscount[discount]
        money_saved = flatdiscount[discount]
    else:
        total_price = subtot
        money_saved = 0
    
    approx_time = approximate_time(choice)

    print(f"Welcome to Chipotle Mexican Grill Hadley, {customer_name}.")
    print("Your invoice is displayed below:")
    print(f"Protein: {protein} - ${pprice}")
    print(f"Rice: {rice} rice - ${rprice}")
    print(f"Beans: {beans} beans - ${bprice}")
    print(f"Burrito: {'Yes' if burrito else 'No'} - ${burprice}")
    print(f"Toppings: {', '.join(toppings)} - ${topprice}")
    print(f"Subtotal: ${subtot}")
    print(f"Discount Code: {discount}")
    print(f"Total: ${total_price}")
    print(f"You Save: ${money_saved}")
    print(f"Your order will be ready in {approx_time} minutes.")
    print("Enjoy your meal and have a good day!")


generate_invoice(order1)