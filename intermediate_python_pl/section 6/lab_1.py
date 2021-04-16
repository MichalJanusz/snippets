cake_01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7,
}
cake_02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3,
}


def show_cake_info(cake):
    print(f'{cake["taste"]} cake with {cake["glaze"]} glaze with text \"{cake["text"]}\" of {cake["weight"]} kg')


cakes = [cake_01, cake_02]

for cake in cakes:
    show_cake_info(cake)
