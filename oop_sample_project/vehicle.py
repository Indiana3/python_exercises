class Fruit:
    def __init__(self, name, brand, is_season, is_biological):
        self.name = name
        self.brand = brand
        self.is_season = is_season
        self.is_biological = is_biological
    
    def __str__(self):
        return "Name: {}, Brand: {}, Is season? {}, Is biological? {}".format(self.name, self.brand, self.is_season, self.is_biological)

fruit_1 = Fruit("apple", "Pinklady", True, False)
print(fruit_1)