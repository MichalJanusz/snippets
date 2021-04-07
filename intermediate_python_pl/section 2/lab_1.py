print('1. zmienne jedna linijka')
a = b = c = 10
print(a, b, c)
print(id(a), id(b), id(c))

a = 20

print(a, b, c)
print(id(a), id(b), id(c))

print('')

print('2. lista')
a = b = c = [10, 20, 30]
print(a, b, c)
print(id(a), id(b), id(c))

a.append(40)

print(a, b, c)
print(id(a), id(b), id(c))

print('')

print('3. zmienne rozne linijki')
x = 10
y = 10
print(id(x), id(y))

print('')
print('4. y+1-1')
y = y + 1 - 1
print(id(x), id(y))

print('')
print('5. y+1234567890-1234567890')
y = y + 123456 - 123456
print(id(x), id(y))
