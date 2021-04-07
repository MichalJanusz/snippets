def display_options(options):
    for i in range(len(options)):
        print(f'{i+1} - {options[i]}')

    choice = input('Select option above or press enter to exit:')

    return choice


options = ['load data', 'export data', 'analyze & predict']

choice = 'x'

while choice:

    choice = display_options(options)

    if choice:
        try:
            choice_num = int(choice)
            if 0 < choice_num <= len(options):
                print(f"you have selected {choice_num} - {options[choice_num-1]}")
            else:
                print('choose a value from the list')
        except:
            print('please enter a number')
    else:
        print('exit')

