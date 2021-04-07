colors = ["red", "orange", "green", "violet", "blue", "yellow"]


def how_many_colors(color_list, n):
    return color_list[:n]


for i in range(1, len(colors) + 1):
    print(how_many_colors(colors, i))

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja'

print(definition[definition.index('(')+1:definition.index(')')])
