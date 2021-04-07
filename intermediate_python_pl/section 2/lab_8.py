projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

# for proj, lead in zip(projects, leaders):
#     print(f'The leader of {proj} is {lead}')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for num, (proj, date, lead) in enumerate(zip(projects, dates, leaders), 1):
    print(f'{num} - The leader of {proj}  started {date} is {lead}')
