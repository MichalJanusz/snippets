class NoDuplicates:

    def __init__(self):
        self.items = []

    def __call__(self, new_items):
        for item in new_items:
            if item not in self.items:
                self.items.append(item)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.items)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.items)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.items)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.items)

