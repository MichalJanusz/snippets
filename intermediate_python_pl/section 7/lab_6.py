class Cake:
    """Cake class used for storing info about cakes avaliable in the bakery"""

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        init method attributes:
        :param name: Name of the cake
        :param kind: kind of the cake
        :param taste: taste of the cake
        :param additives: what additives the cake does have
        :param filling: what is the filling of the cake
        """

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        """

        :return: Returns formatted name of the cake
        """

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


help(Cake)
help(Cake.full_name)
