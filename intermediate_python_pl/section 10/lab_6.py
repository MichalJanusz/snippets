import itertools as it


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


# candidate_list = list(range(1, 10001))
#
# filtered_list = list(it.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))
#
# print(filtered_list)
#
# for elem in filtered_list:
#     print(elem, get_factors(elem))


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


prime_numbers = list(it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 100001)), 10))

print(prime_numbers)
