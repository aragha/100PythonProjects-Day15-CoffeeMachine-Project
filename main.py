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
    :return: boolean True if resources are available
    boolean False if resources are insufficient
    """
    if drink_request == 'espresso':
        if MENU['espresso']['ingredients']['water'] >= 50 and MENU['espresso']['ingredients']['coffee'] >= 18:
            return True
        else:
            return False
    elif drink_request == 'latte':
        if MENU['latte']['ingredients']['water'] >= 200 and MENU['latte']['ingredients']['milk'] >= 150  and MENU['latte']['ingredients']['coffee'] >= 24:
            return True
        else:
            return False
    else:
        if MENU['cappucino']['ingredients']['water'] >= 250 and MENU['cappucino']['ingredients']['milk'] >= 100  and MENU['cappucino']['ingredients']['coffee'] >= 24 :
            return True
        else:
            return False


def make_coffee(drink_request):
    global resources

    if drink_request == 'espresso':
        resources['water'] -= 50
        resources['coffee'] -= 18
    elif drink_request == 'latte':
        resources['water'] -= 200
        resources['coffee'] -= 24
        resources['milk'] -= 150
    else:
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 100


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


drinkslist = ['espresso', 'latte', 'cappuccino']
if __name__ == '__main__':
    print_report()
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
        print("Please insert coins.")
        q = float(input("How many quarters: "))
        d = float(input("How many dimes: "))
        n = float(input("How many nickels: "))
        p = float(input("How many pennies: "))
        transaction_status = []
        transaction_status = process_coins(drink, q, d, n, p)
        if transaction_status[0]:
            if transaction_status[1] == 0:
                print(f"Here is your {drink} ☕️. Enjoy!")
            else:
                print(f"Here is your {drink} ☕ and here is your change {transaction_status[1]}️. Enjoy! ")
        else:
            print("Sorry that's not enough money. Money refunded.")
        print_report()
        drink = input("What would you like? (espresso/latte/cappuccino): ")