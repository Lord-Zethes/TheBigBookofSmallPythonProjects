import datetime
import random
## Constant Array -> Months never change
MONTHS_IN_ORDER = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


def intro():
    """This Function just prints the intro nothing special here"""
    print('The Birthday Paradox shows us that in a group of n people, the odds\n'
          'that two of them have a matching birthday is surprisingly large.\n'
          'This program runs a Monte Carlo simulation (repeated random\n'
          'simulations) to explore this concept.\n'
          "(It's not actually a paradox, it is just a surprising result.)")

def get_birthdays(number_of_birthdays):
    """Returns a list of random birthdays."""
    birthdays = []
    for _ in range(number_of_birthdays):
        start_of_year = datetime.date(1998, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    """Returns the date of a birthday that happens more than once, or None."""
    birthday_count = {}
    for birthday in birthdays:
        if birthday in birthday_count:
            return birthday
        birthday_count[birthday] = 1
    return None

def main():
    """Responsible for putting all my subfunctions together and running the meat and potatos of the program"""
    intro()
    
    while True:
        print("How many birthdays shall I generate? (Choose between 1 and 100)")
        response = input()
        if response.isdecimal() and 0 < int(response) <= 100:
            num_bdays = int(response)
            break
        else:
            print("Please enter a number between 1 and 100.")
    
    print()
    print("Here are", num_bdays, "birthdays:")
    
    birthdays = get_birthdays(num_bdays)
    for i, birthday in enumerate(birthdays):
        if i > 0:
            print(', ', end='')
        month_name = MONTHS_IN_ORDER[birthday.month - 1]
        print(f"{month_name} {birthday.day}", end='')
    print("\n")
    
    match = get_match(birthdays)
    print("In this simulation, ", end='')
    if match:
        month_name = MONTHS_IN_ORDER[match.month - 1]
        print(f'multiple people have a birthday on {month_name} {match.day}.')
    else:
        print("there is no matching birthday.")
    
    print("\nGenerating", num_bdays, "random birthdays 100,000 times...")
    input('Press Enter to begin...')
    
    print("Let's run another 100,000 simulations.")
    sim_match = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, "simulations run.")
        birthdays = get_birthdays(num_bdays)
        if get_match(birthdays):
            sim_match += 1
            
    print("100,000 simulations run.")
    
    probability = round(sim_match / 100_000 * 100, 2)
    print(f'Out of 100,000 simulations of {num_bdays} people, there was a\n'
          f'matching birthday in that group {sim_match} times. This means\n'
          f'that {num_bdays} people have a {probability}% chance of\n'
          'having a matching birthday in their group.')
    print("That's probably more than you think.")


main()
