import re
from collections import defaultdict
from heapq import heappush, heappop

with open("input.txt", "r") as file:
    lines = file.read().split("\n")

# PART 1

PATTERN = r"(\w+),?\s?\.?"

potential_allergens = {}
food_occurrences = defaultdict(int)
for line in lines:
    unknown_ingredients, allergens = line.split(" (contains ")
    unknown_ingredients = set(unknown_ingredients.split())
    for unknown_food in unknown_ingredients:
        food_occurrences[unknown_food] += 1
    for allergen in re.findall(PATTERN, allergens):
        if allergen not in potential_allergens:
            potential_allergens[allergen] = set(unknown_ingredients)
        else:
            potential_allergens[allergen] &= unknown_ingredients

allergens = reduce(lambda x,y: x | y, potential_allergens.values())

non_allergens = set()
for line in lines:
    unknown_ingredients = set(line.split(" (contains ")[0].split())
    non_allergens |= unknown_ingredients - allergens
    
print("PART 1", sum(food_occurrences[v] for v in non_allergens))

# PART 2

ordered_allergens = []
already_matched_ingredient = ""
while potential_allergens:
    found_allergen = True
    for allergen, unknown_ingredients in potential_allergens.items():
        unknown_ingredients.discard(already_matched_ingredient)
        if len(unknown_ingredients) == 1 and found_allergen:
            newly_found_allergen, matched_ingredient = allergen, unknown_ingredients.pop()
            found_allergen = False
    heappush(ordered_allergens, (newly_found_allergen, matched_ingredient))
    potential_allergens.pop(newly_found_allergen)
    already_matched_ingredient = matched_ingredient

res = ""
while ordered_allergens:
    res += heappop(ordered_allergens)[1] + ","

print("PART 2", res[:-1])