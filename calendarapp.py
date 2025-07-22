# Inform user of the alternatives they have.
def print_options():
    print('1. Lägg till en händelse')
    print('2. Visa alla händelser')
    print('3. Sök efter en händelse')
    print('4. Filtrera och visa händelser efter datum')
    print('5. Räkna och visa totalt antal händelser')
    print('6. Avsluta')

def add_event(calendar: list):
    title = input('Ange händelsetitel: ').strip()
    date = input('Ange datum (YYYY-MM-DD): ').strip()
    description = input('Ange beskrivning: ').strip()

    event = [title, date, description]

    # Exclude invalid events.
    if not title == '' and not date == '':
        calendar.append(event)
        print('Händelse tillagd!')
    else:
        print('Ogiltigt försök att lägga till en händelse.')
    
# Help function to call instead of repeating code. 
def print_an_event(event: list):
    print(f'Title: {event[0]}, Datum: {event[1]}, Beskrivning: {event[2]}')

def print_all_events(calendar: list):
    for event in calendar:
        print_an_event(event)

# Find and print all events containing a title key from user.
def search_for_event(calendar: list):
    search_key = input('Ange händelsetitel: ').strip()
    print('Resultat:')

    for event in calendar:
        if search_key in event[0]:
            print_an_event(event)

# Find and print all events after a given date (including the date given).
def filter_by_date(calendar: list):
    filter_key = input('Ange datum (YYYY-MM-DD): ').strip()
    # Compare key to all events in calendar.
    for event in calendar:
        if filter_key <= event[1]:
            print_an_event(event)
        
# This function is only here because the assignment stated that we had to have a function to count.
# Otherwise I would hae just used len(calendar).
def count_number_of_events(calendar: list) -> int:
    number_of_events = 0
    for event in calendar:
        number_of_events += 1
    return number_of_events

# Dealing with the menu.
def __main__():
    calendar = list() 
    while True:

        print_options()
        action = input('Välj ett alternativ: ')
        match action:
            case '1':
                add_event(calendar)
            case '2':
                print_all_events(calendar)
            case '3':
                search_for_event(calendar)
            case '4':
                filter_by_date(calendar)
            case '5':
                number_of_events = count_number_of_events(calendar) 
                print(f'Totalt antal händelser i kalendern: {number_of_events}')
            case '6':
                break
            # case _:
        
        print()     # Just an empty line for the format

if __name__ == "__main__":
    __main__()    