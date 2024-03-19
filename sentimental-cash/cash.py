import cs50


def main():
    # functions
    cents = get_cents()
    # quarter function
    quarters = cal_quarters(cents)
    cents = cents-quarters*25
    # dimes function
    dimes = cal_dimes(cents)
    cents = cents-dimes*10
    # nickle function
    nickles = cal_nickles(cents)
    cents = cents-nickles*5
# pennies function
    pennies = cal_pennies(cents)
    cents = cents-pennies*1
# calculating coin formula
    coins = quarters+dimes+nickles+pennies

    print(int(coins))
# defining functions


def get_cents():
    # getting cash from user and cash is always greater then 0
    cash = cs50.get_float("Enter amount :")
    while (cash <= 0):
        cash = cs50.get_float("Enter Valid amount: ")
    cents = cash*100
    return cents
# defining functions of calculating quarters , dimes ,nickles and pennies


def cal_quarters(cents):
    # dividing total cents by 25 to get number of quarters
    quarters = cents/25
    return int(quarters)

# dividing remaining cents by 10 to get number of dimes
def cal_dimes(cents):
    dimes = cents/10
    return int(dimes)

# dividing remaining cents by 5 to get number of nickles
def cal_nickles(cents):
    nickles = cents/5
    return int(nickles)

# dividing remaining cents by 1 to get number of pennies
def cal_pennies(cents):
    pennies = cents/1
    return int(pennies)


main()
