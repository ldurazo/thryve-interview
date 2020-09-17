from api.models.food_nutrient import FoodNutrient


class Nutrient:
    id = None
    name = None
    food_nutrients = None

    def __init__(self, nutrient_id, name):
        self.id = int(nutrient_id)
        self.name = name
        self.food_nutrients = []

    def append_food(self, food, amount, unit):
        self.food_nutrients.append(FoodNutrient(food, self.id, amount, unit))

    def serialize(self, flatten_by_food=None):
        serialized_nutrient = {
            'id': self.id,
            'name': self.name,
        }
        if flatten_by_food is not None:
            food_nutrient = next((item for item in self.food_nutrients if item.food_name == flatten_by_food), None)
            serialized_nutrient['amount'] = food_nutrient.amount
            serialized_nutrient['unit'] = food_nutrient.unit
        else:
            serialized_nutrient['food_nutrients'] = [food_nutrient.serialize() for food_nutrient in self.food_nutrients]
        return serialized_nutrient

    def __str__(self) -> str:
        return 'id %s, name %s' % (self.id, self.name)
