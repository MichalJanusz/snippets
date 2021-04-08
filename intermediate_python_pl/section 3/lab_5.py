import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range(1000000):
    argument_list.append(i/10)

print('uncompiled')
for formula in formulas_list:

    results_list = []
    print(f'Formula {formula}')
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print(f'min = {min(results_list)} max = {max(results_list)}')
    stop = time.time()
    print(f'Calculation time: {stop - start}')

print('compiled')
for formula in formulas_list:

    results_list = []
    print(f'Formula {formula}')
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print(f'min = {min(results_list)} max = {max(results_list)}')
    stop = time.time()
    print(f'Calculation time: {stop - start}')
