def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8

transformations = [double, root, div2, negative]

tmp_return_value = number

for transormation in transformations:
    tmp_return_value = transormation(tmp_return_value)
    print(tmp_return_value)


transformations = [root, root, div2, double]

tmp_return_value = number

for transormation in transformations:
    tmp_return_value = transormation(tmp_return_value)
    print(tmp_return_value)
