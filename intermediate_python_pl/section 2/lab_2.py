days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

# creating a copy of the list
workdays = days.copy()

workdays.remove('sat')
workdays.remove('sun')

print(days)
print(workdays)
