from menu import MENU, resources, money

def print_report():
    """
    When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values. e.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    """
    # print(f"---------------------")
    print(f"Our resources report:")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Cash: {money}")
    print(f"---------------------")
# Press the green button in the gutter to run the script.

def check_resources(drink_request):
    """
    :param drink_request: String indicating what drink was requested Eg: "latte"
    :return: integer 0 if successfull
     1: if we're out of water
     2: if we're out of milk
     3: if we're out of coffee
    """
    global resources
    if drink_request == 'espresso':
        if resources['water'] >= 50:
            if  resources['coffee'] >= 18:
                return 0
            else:
                return 3
        else:
            return 1
    elif drink_request == 'latte':
        if resources['water'] < 200:
            return 1
        elif resources['milk'] < 150:
            return 2
        elif resources['coffee'] < 24:
            return 3
        else:
            return 0
    else:
        if resources['water'] < 250:
            return 1
        elif resources['milk'] < 200:
            return 2
        elif resources['coffee'] < 100:
            return 3
        else:
            return 0


def make_coffee(drink_request):
    global resources
    goahead = check_resources(drink_request)
    # print(f"goahead: {goahead}")
    if goahead == 0:
        if drink_request == 'espresso':
            resources['water'] -= 50
            resources['coffee'] -= 18
        elif drink_request == 'latte':
            resources['water'] -= 200
            resources['coffee'] -= 24
            resources['milk'] -= 150
        elif drink_request == 'cappuccino':
                resources['water'] -= 250
                resources['coffee'] -= 24
                resources['milk'] -= 100
    return goahead
        #
        # print("Need to restock kitchen. Here's your refund")

def process_coins(drink_request, q, d, n, p):
    """
    :param drink_request: string indicating which drink was requested
    :param q: number of quarters
    :param d: number of dimes
    :param n: number of nickels
    :param p: number of pennies
    :return: difference if enough money has been deposited. the money deposited, otherwise
    """
    global money
    money_deposited = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    result_list = []
    if money_deposited >= MENU[drink_request]['cost']:
        money += MENU[drink_request]['cost']
        # print(money)
        result_list.append(True)
        result_list.append(money_deposited - MENU[drink_request]['cost'])
    else:
        result_list.append(False)
        result_list.append(money_deposited)
    return (result_list)

def take_orders(dr):
    production_status = 0
    production_status = make_coffee(dr)
    if production_status == 0:
        print("Please insert coins.")
        q = float(input("How many quarters: "))
        d = float(input("How many dimes: "))
        n = float(input("How many nickels: "))
        p = float(input("How many pennies: "))

        transaction_status = []
        transaction_status = process_coins(dr, q, d, n, p)
        if transaction_status[0]:
            if transaction_status[1] == 0:
                print(f"Here is your {dr} ☕️. Enjoy!")
            else:
                print(f"Here is your {dr} ☕ and here is your change {transaction_status[1]}️. Enjoy! ")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        restock_message={1: "Sorry, we're out of water", 2: "Sorry, we're out of milk",1: "Sorry, we're out of coffee"}
        print(f'{restock_message[production_status]}.')
    print_report()
    drink = input('What would you like? (espresso/latte/cappuccino): ')
    return drink

drinkslist = ['espresso', 'latte', 'cappuccino']
if __name__ == '__main__':
    # print_report()
    # for d in drinkslist:
    #     print(check_resources("espresso"))
    # for d in drinkslist:
    #     make_coffee(d)
    #     print_report()
    # for d in drinkslist:
    #     # print(process_coins(d, 4, 10, 20, 200))
    #     print(process_coins(d, 4, 0, 0, 0))
    #     print_report()
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    while drink in drinkslist:
        drink = take_orders(drink)
