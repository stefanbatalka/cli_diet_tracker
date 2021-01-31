# cli_diet_tracker
simple CLI diet tracker

# Usage

Calling main.py like python3 main.py COMMAND VARIABLES
### foods
Show all foods in database
### meals
Show all meals in database

### add_food NAME PROTEIN CARBS FAT CALS
Adds a new food to db

### create_meal NAME *FOOD_IDs
Creates a meal from existing food components

### consume_meal MEAL_ID
Consumes a given meal by ID, use if you know the ID of the meal

### eat
Select from meals in db to consume at this time, use if you are not sure of the meal-ID in db



