# x = []
# y = (input('hi: ')),
# x += y
# x

# from constants import *

# recipe_collection = [
#     CHOCOLATE_PEANUT_BUTTER_SHAKE, 
#     BROWNIE, 
#     SEITAN, 
#     CINNAMON_ROLLS, 
#     PEANUT_BUTTER, 
#     MUNG_BEAN_OMELETTE
# ]

# BROWNIE = ('chocolate brownies',
# 	'2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,80 g Nuttelex,125 g self-raising flour,70 g ground almonds,50 g cocoa powder,0.2 tsp baking powder,250 g sugar,1.5 tsp vanilla extract')

# test = BROWNIE[1].split(",")

def test(z: int) -> tuple(list[float, float]):
    x = 2*z
    y = 3*z
    q  = ([x], [y])
    print(type(q))
    return q

num1, num2 = test(2)
help_1 = ("H hor h                         : Help")
help_2 = ("\nH hor h                         : Help")
help_test = help_1+help_2
print(help_test)