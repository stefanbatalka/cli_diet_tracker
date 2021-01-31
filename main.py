import fire

from db import FoodFactory

import food

print("Connecting")
db = FoodFactory()

def meals():    
    for idx, meal in enumerate(db.get_all_meals()):
        print(f"{idx} : {meal}")

def foods():
    for idx, food in enumerate(db.get_all_foods()):
        print(f"{idx} : {food}")

def add_food(name, protein, carbs, fat, cals):
    new_food = food.Food(name, protein, carbs, fat, cals)
    
    print("Created food:", new_food)

    db.add_food(new_food)

def create_meal(name, *foodcomponents):

    all_foods = [n for n in db.get_all_foods()]

    these_components = []

    for component_id in foodcomponents:
        these_components.append(all_foods[component_id])

    new_meal = food.Meal(name, these_components)

    print("Created meal:", new_meal)                               

    db.add_meal(new_meal)

def consume_meal(meal_number):

    all_meals = [n for n in db.get_all_meals()]
    this_meal = all_meals[meal_number]

    db.consume(this_meal)

    print("Ate", this_meal)

def eat():
    all_meals = [n for n in db.get_all_meals()]

    for idx, meal in enumerate(all_meals):
        print(f"{idx} : {meal}")

    selected = input("Select meal to consume:")

    this_meal = all_meals[int(selected)]

    db.consume(this_meal)

    print("Ate", this_meal)

if __name__ == "__main__":
    fire.Fire()

