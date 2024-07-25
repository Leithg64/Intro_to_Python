# empty list for ingredients
recipe_list = []

ingredients_list = []

# user input for recipe components
def take_recipe():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the dish's cooking time in minutes: "))
    ingredients = (list(input("Enter the dish's ingredients, separated by a coma: ").split(", ")))
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe

# User prompt
n = int(input("How many recipes will you enter? "))

# Iterates through all recipes given by user
for i in range(n):
    recipe = take_recipe()

    # Checks if an ingredient should be added to the list
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

    recipe_list.append(recipe)

    # Determines difficulty of recipe
    for recipe in recipe_list:
        if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
            recipe["difficulty"] = "Easy"
        elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
            recipe["difficulty"] = "Medium"
        elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
            recipe["difficulty"] = "Intermediate"
        elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
            recipe["difficulty"] ="Hard"

    # Iterate through Recipes_list and display their info
    for recipe in recipe_list:
        print("Recipe: ", recipe["name"])
        print("Cooking Time (minutes): ", recipe["cooking_time"])
        print("Ingredients: ")
        for ingredient in recipe["ingredients"]:
            print(ingredient)
        print("Difficulty: ", recipe["difficulty"])

    # Display ingredients from all recipes in alphabetical order
    def all_ingredients():
        print("Ingredients available across all recipes: ")
        ingredients_list.sort()
        for ingredient in ingredients_list:
            print(ingredient)

all_ingredients()
