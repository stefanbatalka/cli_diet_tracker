from pymongo import MongoClient

from auth import db_uri

import food



class FoodFactory:

    def __init__(self):
        self.master = MongoClient(db_uri)["diettracker"]
        self.food_db = self.master["foods"]
        self.meal_db = self.master["meals"]

    def add_food(self, food: food.Food):
        self.food_db.insert_one(food.__dict__)

    def add_meal(self, meal: food.Meal):
        self.meal_db.insert_one(meal.__dict__)

    def remove_food(self, uid):
        self.food_db.remove({"_id": uid})
    
    def remove_meal(self, uid):
        self.meal_db.remove({"_id": uid})

    def get_all_foods(self):
        all_foods = self.food_db.find({})

        for food in all_foods:
            yield food
        
    def get_all_meals(self):
        all_meals = self.meal_db.find()

        for meal in all_meals:
            yield meal

    def get_all_meals_by_day(self):
        raise NotImplementedError

if __name__ == "__main__":

    factory = FoodFactory()

    print("All foods")
    for food in factory.get_all_foods():
        print(food)

    print("All meals")
    for meal in factory.get_all_meals():
        print(meal)

