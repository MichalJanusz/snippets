# Fibonnaci sequence functions and generators


# infinite fibonacci generator
def fib():
    n2 = 0
    n3 = 1
    while True:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        yield n1


# fibonnaci generator with specified range
def fibonnaci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
