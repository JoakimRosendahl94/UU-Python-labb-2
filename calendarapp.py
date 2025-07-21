def print_options():
    print('1. Lägg till en händelse')
    print('2. Visa alla händelser')
    print('3. Sök efter en händelse')
    print('4. Filtrera och visa händelser efter datum')
    print('5. Räkna och visa totalt antal händelser')
    print('6. Avsluta')

def add_event(calendar):
    title = input('Ange händelsetitel: ').strip()
    date = input('Ange datum (YYYY-MM-DD): ').strip()
    description = input('Ange beskrivning: ').strip()

    if not title == '' and not date == '':
        calendar.append([title, date, description])
        print('Händelse tillagd!')
    else:
        print('Ogiltigt försök att lägga till en händelse.')
    

def print_an_event(event):
    print(f'Title: {event[0]}, Datum: {event[1]}, Beskrivning: {event[2]}')

def show_all_events(calendar):
    for event in calendar:
        print_an_event(event)

def search_for_event(calendar):
    search_key = input('Ange händelsetitel: ').strip()
    print('Resultat:')

    for event in calendar:
        if search_key in event[0]:
            print_an_event(event)

def filter_by_date(calendar):
    filter_key = input('Ange datum (YYYY-MM-DD): ').strip()
    keys_list = list()
    keys_list = filter_key.split('-')
    keys_list = [int(element) for element in keys_list]

    for event in calendar:
        for index in range(len(keys_list)):
            date = event[1].split('-')
            date = [int(element) for element in date]

            if not keys_list[index] <= date[index]:
                index = len(keys_list) - 1
                break
            else:
                print_an_event(event)

def __main__():
    calendar = list() 
    while True:

        print_options()
        action = input('Välj ett alternativ: ')
        match action:
            case '1':
                add_event(calendar)
            case '2':
                show_all_events(calendar)
            case '3':
                search_for_event(calendar)
            case '4':
                filter_by_date(calendar)
            case '5':
                print(f'Totalt antal händelser i kalendern: {len(calendar)}')
            case '6':
                break
            # case _:
        
        print()     # Just an empty line for the format


__main__()    