import pickle
import glob


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'tart', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additions, filling, gluten_free, text):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additions = additions
        self.filling = filling
        self.__gluten_free = gluten_free
        if kind == 'cake' or len(text) == 0:
            self.__text = text
        else:
            self.__text = ''
            print(f'text can be set only for cake ({name})')
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(f'{self.name.upper()}')
        print(f'Kind:     {self.kind}')
        print(f'Taste:    {self.taste}')
        if len(self.additions) > 0:
            print("Additions:")
            for a in self.additions:
                print(f"\t{a}")
        if len(self.filling) > 0:
            print(f'Filling:  {self.filling}')
        print(f'Gluten Free: {self.__gluten_free}')
        if len(self.__text) > 0:
            print(f'Text:     {self.__text}')
        print('-' * 20)

    def set_filling(self, new_filling):
        self.filling = new_filling

    def add_additives(self, new_additions):
        self.additions.extend(new_additions)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print(f'text can be set only for cake ({self.name})')

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog+'/*.bakery')


pavlova = Cake('Pavlova', 'meringue', 'fruit meringue', ['raspberries', 'blueberries'], '', True, '')
black_forest = Cake('Black Forest', 'cake', 'chocolate', ['cherries'], 'cream', False, 'Happy B-Day!')
lemon_tart = Cake('Lemon tart', 'tart', 'lemon', [], 'lemon curd', True, 'Lemon')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, '')

pavlova.set_filling('vanilla cream')
lemon_tart.add_additives(['mini meringues', 'lemon zest'])

print('Today in our offer:')
for cake in Cake.bakery_offer:
    cake.show_info()

print('-'*30)
print('isinstance: ', isinstance(pavlova, Cake))
print('type: ', type(pavlova) is Cake)
print('-'*15)
print('vars pavlova', vars(pavlova))
print('vars Cake', vars(Cake))
print('dir pavlova', dir(pavlova))
print('dir Cake', dir(Cake))

print('-'*30)

pavlova.__gluten_free = False
print(dir(pavlova))
pavlova._Cake__gluten_free = False
pavlova.show_info()

print('-'*30)

pavlova.Text = 'Test text'
black_forest.Text = 'Merry Christmas'

for cake in Cake.bakery_offer:
    cake.show_info()

print('-'*30)

pavlova.save_to_file('lab_7/pavlova.bakery')
black_forest.save_to_file('lab_7/black_forest.bakery')

cake05 = Cake.read_from_file('lab_7/pavlova.bakery')
cake05.show_info()

print(Cake.get_bakery_files('lab_7'))


