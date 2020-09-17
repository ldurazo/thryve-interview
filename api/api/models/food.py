class Food:
    name = None
    nutrients = None

    def __init__(self, name):
        self.name = name
        self.nutrients = []

    def append_nutrient(self, nutrient):
        self.nutrients.append(nutrient)

    def serialize(self):
        return {
            'name': self.name,
            'nutrients': [nutrient.serialize(flatten_by_food=self.name) for nutrient in self.nutrients],
        }

    def __str__(self) -> str:
        return 'name %s' % self.name
