import os

from flask import json

from api.models.food import Food
from api.models.nutrient import Nutrient
from api.stores.base_store import BaseStore


class StubStore(BaseStore):
    store_nutrients = []
    store_foods = []
    """
    Our implementation to get ingredients and food used by our API
    """

    @classmethod
    def get_foods(cls, conditions) -> set:
        if cls.store_foods.__len__() == 0:
            cls.populate_store()
        foods = cls.filter_by_conditions(conditions)
        return foods

    @classmethod
    def filter_by_conditions(cls, conditions) -> set:
        filtered_foods = set()
        chain_operator = None
        # Check all the conditions
        for idx, condition in enumerate(conditions):
            nutrient_to_check = next(
                (nutrient for nutrient in cls.get_nutrients() if condition['nutrient'] == nutrient.id),
                None)
            food_nutrients = nutrient_to_check.food_nutrients if nutrient_to_check is not None else None

            # Handle the very first case, chain operator functions as a tail recursion arg.
            if idx == 0:
                filtered_foods = set([food for food in food_nutrients if cls.passes_condition(condition, food)])
            else:
                # If the operator is an or, grab the condition values and add them to the previous result
                if chain_operator == 'or':
                    filtered_foods = filtered_foods.union(
                        set([food for food in food_nutrients if cls.passes_condition(condition, food)]))

                # If the operator is and, filter by the previously filtered food, to further execute the filter logic
                elif chain_operator == 'and':
                    filtered_foods = set([food for food in filtered_foods if cls.passes_condition(condition, food)])
            chain_operator = condition['chain_operator'] if condition.__contains__('chain_operator') else None

        return filtered_foods

    @classmethod
    def passes_condition(cls, condition, food_nutrient) -> bool:
        if condition['operator'] == '=':
            return food_nutrient.amount == condition['value']
        if condition['operator'] == '>':
            return food_nutrient.amount > condition['value']
        if condition['operator'] == '<':
            return food_nutrient.amount < condition['value']
        if condition['operator'] == '>=':
            return food_nutrient.amount >= condition['value']
        if condition['operator'] == '<=':
            return food_nutrient.amount <= condition['value']
        pass

    @classmethod
    def get_nutrients(cls) -> list:
        """ Better do it once than with every request """
        if cls.store_nutrients.__len__() == 0:
            cls.populate_store()
        return cls.store_nutrients

    @classmethod
    def populate_store(cls):
        filename = os.path.join('./api/resources', 'food_data.json')
        with open(filename) as food_data:
            foods = json.load(food_data)

        def find_nutrient_in_store(search_item):
            return next((item for item in cls.store_nutrients if
                         item.id == int(search_item['nutrient_id'])), None)

        def find_food_in_store(search_item):
            return next((item for item in cls.store_foods if
                         item.name == search_item['name']), None)

        # Even though we technically have a ~O(n^2) complexity for nutrition population, it's the only way
        # to traverse the matrix formed by food and nutrients, in order to reverse engineer the nutrient instances
        # into a format that is more advantageous to the problem at hand.
        for food_d in foods['report']['foods']:
            food = find_food_in_store(food_d)
            if not food:
                food = Food(food_d['name'])
                cls.store_foods.append(food)
            for nutrient_d in food_d['nutrients']:
                nutrient = find_nutrient_in_store(nutrient_d)
                if not nutrient:
                    nutrient = Nutrient(nutrient_d['nutrient_id'], nutrient_d['nutrient'])
                    cls.store_nutrients.append(nutrient)
                nutrient.append_food(food_d['name'], nutrient_d['value'], nutrient_d['unit'])
                food.append_nutrient(nutrient)
