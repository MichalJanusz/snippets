import math

argument_list = [i/10 for i in range(100)]

formula = input("Please enter the formula, use x as the argument: ")


for x in argument_list:
    print(f"{x:3.1f} {eval(formula):6.2f}")


