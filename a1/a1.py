"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Bejnamin Burn"
__email__ = "b.burn@uqconnect.edu.au"
__date__ = "03/03/2023"

from constants import *

# Write your functions here

command = {
    'H' : 0,
    'h' : 0,
    'mkrec' : 1,
    'add' : 2,
    'rm' : 3,
    'rm -i' : 4,
    'ls' : 5,
    'ls -a' : 6,
    'ls -s' : 7,
    'G' : 8,
    'g' : 8,
    'Q' : 9,
    'q' : 9
}

help1 = ("    H or h: Help")
help2 = ("\n    mkrec: creates a recipe, add to cook book.")
help3 = ("\n    add {recipe}: adds a recipe to the collection.")
help4 = ("\n    rm {recipe}: removes a recipe from the collection.")
help5 = ("\n    rm -i {ingredient_name} {amount}: removes ingredient from shopping list.")
help6 = ("\n    ls: list all recipes in shopping cart.")
help7 = ("\n    ls -a: list all available recipes in cook book.")
help8 = ("\n    ls -s: display shopping list.")
help9 = ("\n    g or G: generates a shopping list.")
help10 = ("\n    Q or q: Quit.")
help = help1 + help2 + help3 + help4 + help5 + help6 + help7 + help8 + help9 + help10

def num_hours() -> float:
    """
    Retruns the number of hours this student 
    slaved away on this assignment.
    """
    return 10

def get_recipe_name(recipe: tuple[str, str]) -> str:
    """
    Given the recipe returns the name of the recipe.
    """
    return recipe[0]

def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """
    Breaks down the raw ingredients into: amount, measure, ingredient.
    """
    rid = raw_ingredient_detail
    parse1, parse2 = rid.split(" ", 1)
    parse3, parse4 = parse2.split(" ", 1)
    parsed_ingredient = float(parse1), parse3, parse4
    return parsed_ingredient

def create_recipe() -> tuple[str, str]:
    """
    Creates a new recipe.
    """
    recipes = ()
    ingredients = ""
    name = (input("Please enter the recipe name: ")),
    recipes += name
    x = 0
    y = 0
    while x == 0:
        ingredient_input = input("Please enter an ingredient: ")
        if ingredient_input == '':
            break
        if y == 0:
            ingredients += ingredient_input
            y += 1
        else:
            ingredients += f",{ingredient_input}"
        join_ingredient = ''.join(ingredients)
    recipes += (join_ingredient),
    return recipes

def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    """
    Returns a list of parse ingredients using the parse_ingredients
    function.
    """
    ingredients = recipe[1]
    ingredient_list = ingredients.split(",")
    new_list = ()
    for i in ingredient_list:
        x = (parse_ingredient(i)),
        new_list += x
    return new_list

def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    """
    Adds a recipe to the list of recipes.
    """
    recipes += (new_recipe),

def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    """
    Returns the recipe with the given name or if the recipe is not
    in the list, returns nothing.
    """
    for i in range(len(recipes)):
        if recipe_name == recipes[i][0]:
            return recipes[i]
    return None

def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """
    Removes the recipe with the given name from the recipe list.
    """
    i = 0
    while i != len(recipes):
        if name == recipes[i][0]:
            recipes.remove(recipes[i])
            break
        i += 1

def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float,
str] | None:
    """
    Returns the amount and measure of an ingredient from a recipe.
    """
    ings = recipe[1]
    split_ings = ings.split(",")
    for i in range(len(split_ings)):
        amount, measure, name = split_ings[i].split(" ")
        if name == ingredient:
            return (float(amount), measure)
    return None

def add_to_shopping_list(ingredient_details: tuple[float, str, str],
shopping_list: list[tuple[float, str, str] | None]) -> None:
    """
    Adds an amount of a given ingredient to the shopping list.
    """
    add_ind = 0 # indicates whether ingredient details matches an ingredient in shopping list
    loc_ind = -1 # records the location of a matched ingredient
    if len(shopping_list) == 0:
        shopping_list.append(ingredient_details)
    else:
        for i in range(len(shopping_list)):
            if ingredient_details[2] == shopping_list[i][2]:
                add_ind += 1
                loc_ind = i         
        if add_ind == 1:
            shopping_list[loc_ind] = (shopping_list[loc_ind][0] + ingredient_details[0], 
            shopping_list[loc_ind][1], shopping_list[loc_ind][2]) 
        else: 
            shopping_list.append(ingredient_details)

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list:
list) -> None:
    """
    Removes an amount of a given ingredient from the shopping list.
    """
    i = 0
    remove_indicator = 0 # indicates whether an ingredient has been removed from the list
    while i != len(shopping_list):
        if str(ingredient_name) == str(shopping_list[i][2]):
            remove_indicator = shopping_list[i][0] - amount
            if remove_indicator <= 0:
                shopping_list.remove(shopping_list[i])
                i -= 1
            else:
                shopping_list[i] = (shopping_list[i][0] - amount, shopping_list[i][1],
                shopping_list[i][2])
        i += 1
   
def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    """
    Returns a list of ingredients made up from the recipes list.
    """
    shopping_list = []
    for i in range(len(recipes)): 
        recipe_ing = recipe_ingredients(recipes[i])
        for i in range(len(recipe_ing)):
            add_to_shopping_list(recipe_ing[i], shopping_list)
    return shopping_list

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """
    Prints the given shopping list in alphabetical order in a neat fasion.
    """
    x = 0   # maximum length for amount
    y = 0   # maximum length for measure
    z = 0   # maximum length for name
    for i in range(len(shopping_list)):
        if len(str(shopping_list[i][0])) > x:
            x = len(str(shopping_list[i][0]))
    for i in range(len(shopping_list)):
        if len(shopping_list[i][1]) > y:
            y = len(shopping_list[i][1])
    for i in range(len(shopping_list)):
        if len(shopping_list[i][2]) > z:
            z = len(shopping_list[i][2])
    for i in range(len(shopping_list)):
        amount = str(shopping_list[i][0])
        adj_amount = f"{amount:>{x}}" 
        measure = shopping_list[i][1]
        adj_measure = f"{measure:^{y+1}}"
        name = shopping_list[i][2]
        adj_name = f"{name:<{z+1}}"
        print("|",adj_amount,"|",adj_measure,"|",adj_name,"|")

def sanitise_command(command: str) -> str:
    """
    Return a standardised command to all lower-case and no leading or trailing white spaces removing
    any numbers from the string.
    """
    i = 0
    new_string = ""
    while i != len(command):
        for x in range(10):
            if command[i] == str(x):
                i += 1
        else:
            lower = command[i].lower()
            new_string += lower
            i += 1
    return new_string
    # QQQQ try sanitising more



def main(): 
    """
    The cookbook.
    """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    shopping_cart : list[tuple[str, str]]
    shopping_list : list[tuple[float, str, str]]
    shopping_cart, shopping_list = [], []

    while True:
        c = input("Please enter a command: ")
        c_split = c.split(" ")
        if len(c_split) == 1:
            command = c_split[0]
            variable = ""
        else:
            if c_split[1] == "-i":
                command = "rm -i"
                x = 3
                name  = c_split[2]
                while x != len(c_split) - 1:
                    name += " "
                    name += c_split[x]
                    x += 1
                f_ind = 0
                am_t = c_split[len(c_split)-1]
                am_len = len(am_t)
                for i in am_t:
                    for x in range(10):
                        if str(x) != i:
                            f_ind += 1
                if f_ind >= 10*am_len:
                    amount = False
                else:
                    amount = float(c_split[len(c_split) - 1])
                # print(f"name is {name}")
                # print(f"amount is {amount}")
            elif c_split[1] == "-a":
                command = "ls -a"
                variable = ""
            elif c_split[1] == "-s":
                command = "ls -s"
                variable = ""
            elif c_split[0] == "add":
                command = "add"
                variable = ""
                x = 0
                while x != len(c_split):
                    if x == (len(c_split) - 1):
                        variable += ""
                        break
                    elif x == 0:
                        variable += c_split[x+1]
                        x += 1
                    else:
                        variable += " "
                        variable += c_split[x+1]
                        x += 1
            elif c_split[0] == "rm":
                command = "rm"
                new = c_split[2:]
                variable = c_split[1]
                for i in range(len(new)):
                    variable += f" {new[i]}"
            else:
                command = c_split[0]
                variable = ""
        if command.upper() == 'H': 
            print(help)
        elif command == "mkrec":
            copy_indicator = 0
            new_rec = create_recipe()
            for i in range(len(recipe_collection)):
                if new_rec[0] == recipe_collection[i][0]:
                    copy_indicator += 1
            if copy_indicator == 1:
                None
            else:
                recipe_collection += (new_rec),
        elif command == "add":
            san_var = sanitise_command(variable)
            within_indicator = 0
            for i in range(len(recipe_collection)):
                if san_var == recipe_collection[i][0]:
                    within_indicator += 1
            if within_indicator == 0:
                print("\nRecipe does not exist in the cook book. \nUse the mkrec command to create a new recipe.\n")
            else: 
                add_rec = find_recipe(san_var, recipe_collection) 
                add_recipe(add_rec, shopping_cart)
        elif command == "rm":
            san_var = sanitise_command(variable)
            if shopping_cart == []:
                None
            elif len(shopping_cart) == 1 and san_var == shopping_cart[0][0]:
                shopping_cart = []
                shopping_list = []
            else:
                rem_rec = san_var
                rec_f = find_recipe(rem_rec, recipe_collection)
                rec_ing = recipe_ingredients(rec_f)
                for i in range(len(rec_ing)):
                    remove_from_shopping_list(rec_ing[i][2], 99999, shopping_list)
                remove_recipe(rem_rec, shopping_cart)
                
        elif command == "rm -i":
            match_ind = 0
            if amount == False:
                None
            if shopping_list == []:
                None
            else:
                for i in range(len(shopping_list)):
                    if str(name) == str(shopping_list[i][2]):
                        match_ind += 1
            if match_ind == 1:
                remove_from_shopping_list(name, amount, shopping_list)
        elif command == "ls":
            if shopping_cart == []:
                print("No recipe in meal plan yet.")
            else:
                print(shopping_cart)
        elif command == "ls -a":
            for i in range(len(recipe_collection)):
                print(f"{recipe_collection[i][0]}")
        elif command == "ls -s":
            display_ingredients(shopping_list)
        elif command.upper() == 'G':
            if shopping_cart == []:
                None
            else:
                shopping_list = generate_shopping_list(shopping_cart)
                display_ingredients(shopping_list)
        elif command.upper() == 'Q':
            break
    return None

if __name__ == "__main__":
    main()