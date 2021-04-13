def calculate_paint(efficency_ltr_per_m2, *args):
    total_area = sum(args)
    result = efficency_ltr_per_m2 * total_area
    return result


print(calculate_paint(0.125, 45, 12, 44))

rooms = [45, 12, 44]
print(calculate_paint(0.125, *rooms))


def log_it(*args):

    path = r'lab_2/log_it.txt'

    with open(path, 'a') as f:

        for line in args:
            f.write(line)
            f.write(' ')

        f.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
