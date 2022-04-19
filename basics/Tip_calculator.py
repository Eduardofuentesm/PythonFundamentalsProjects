import time


def Menu(next_dish):
    
    cost_sub = 0
    count_dish = 0
    while next_dish is True:
        dish = input('Enter the Dish: ')
        cost = float(input('Enter the Cost($): $'))
        cost_sub += cost
        count_dish += 1
        next_dish_type = input('\nAdd another dish? Y(es)/N(o):\nR:/')
        if next_dish_type.upper() == 'Y':
            next_dish = True
            time.sleep(2)
        else:
            next_dish = False
        print('-'*30)
    
    #Propina
    people = input('Number of people to cancel the account?: ')
    people = int(people)
    tip = cost_sub * people * 0.07
    tip = round(tip, 2)
    cost_end = cost_sub
    cost_end = round(cost_end, 2)
    payment = cost_end / people
    payment = round(payment, 2)

    print("\nCalculating...")
    time.sleep(2)

    print(f"\nThe cost of {count_dish} {('dish' if count_dish == 1 else 'dishes')} is $ {cost_end}")
    print(f'\nThe tip is $ {tip}')
    print(f"\neach one must pay ${payment} for the meal")

if __name__ == "__main__":
    print("""
        ***** MENU *****
    -----------------------------
    """)
    next_dish = True
    Menu(next_dish)