# Exercise 1

empty_tuple = ()

sisters = ("Ana", "María", "Lucía")
brothers = ("Carlos", "Javier", "Miguel")

all_siblings = brothers + sisters
print(all_siblings)

print(len(all_siblings))

full_family = all_siblings + ("Dad", "Mom")
print(full_family)

# Exercise 2

*only_siblings, father, mother = full_family
print(only_siblings, father, mother)

fruits = ("Apple", "Banana", "Grape")
vegetables = ("Carrot", "Lettuce", "Tomato")
animal_products = ("Milk", "Cheese", "Eggs")

foods = fruits + vegetables + animal_products
print(foods)

food_list = list(foods)
print(food_list)

middle_item = foods[len(foods)//2] if len(foods) % 2 != 0 else foods[len(foods)//2 - 1: len(foods)//2 + 1]
print(middle_item)

print(food_list[3:-3])

del foods

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)