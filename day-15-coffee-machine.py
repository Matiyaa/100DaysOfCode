def main():
    resources = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0
    }

    drinks = {
        'espresso': {
            'water': 50,
            'coffee': 18,
            'milk': 0,
            'money': 1.5
        },
        'latte': {
            'water': 200,
            'coffee': 24,
            'milk': 150,
            'money': 2.5
        },
        'cappuccino': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
            'money': 3.0
        }
    }

    print('Welcome to the Coffee Machine!')

    while True:
        choice = input('What would you like? (espresso/latte/cappuccino):')
        if choice in drinks:
            if (resources['water'] >= drinks[choice]['water'] and
                    resources['milk'] >= drinks[choice]['milk'] and resources['coffee'] >= drinks[choice]['coffee']):
                print(f'Please insert coins, {choice} costs ${drinks[choice]["money"]}')
                quarters = int(input('How many quarters?: '))
                dimes = int(input('How many dimes?: '))
                nickles = int(input('How many nickles?: '))
                pennies = int(input('How many pennies?: '))
                total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                if total >= drinks[choice]['money']:
                    change = total - drinks[choice]['money']
                    print(f"Here is ${change} in change.")
                    prepare_drink(drinks, resources, choice)
                else:
                    print('Sorry that\'s not enough money. Money refunded.')
            else:
                print('Not enough ingredients. Try again.')
        elif choice == 'report':
            report(resources)
        elif choice == 'off':
            break
        else:
            print('Invalid choice. Try again.')


def report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def prepare_drink(drinks, resources, choice):
    for ingredient in drinks[choice]:
        resources[ingredient] -= drinks[choice][ingredient]
        if ingredient == 'money':
            resources[ingredient] += drinks[choice][ingredient]
    print(f"Here is your {choice}. Enjoy!")


if __name__ == "__main__":
    main()
