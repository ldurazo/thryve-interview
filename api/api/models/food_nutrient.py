class FoodNutrient:
    food_name = None
    nutrient_id = None
    amount = None
    unit = None

    def __init__(self, food_name, nutrient_id, amount, unit) -> None:
        self.food_name = food_name
        self.nutrient_id = int(nutrient_id)
        try:
            float_amount = float(amount)
        except ValueError:
            float_amount = 0.0
        self.amount = float_amount
        self.unit = unit

    def serialize(self):
        return {
            'food_name': self.food_name,
            'nutrient_id': self.nutrient_id,
            'amount': self.amount,
            'unit': self.unit
        }

    def __str__(self) -> str:
        return 'food_name %s, nutrient_id %s, amount %s, unit %s' % (
            self.food_name, self.nutrient_id, self.amount, self.unit
        )
