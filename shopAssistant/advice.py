from . import mealsTypes


class Advice:

    def __init__(self):
        self.name = "none"
        self.mealType = mealsTypes.MealType.All
        self.ingredients = []
