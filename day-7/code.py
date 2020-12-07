import re
from collections import defaultdict

with open("input.txt", "r") as file:
    rules = file.read().split("\n")

CONTENT_MATCHING_PATTERN = "(\d)\s(\w+\s\w+)\sbags?(?:(?:,\s)|\.)+"
BAG_COLOR = "shiny gold"

content_to_container_mapping = defaultdict(set)
container_to_content_mapping = defaultdict(dict)
for rule in rules:
    bag, bag_contents = rule.split(" bags contain ")
    for nr, color in re.findall(CONTENT_MATCHING_PATTERN, bag_contents):
        content_to_container_mapping[color].add(bag)
        container_to_content_mapping[bag][color] = int(nr)

# PART 1
def get_nr_bag_colors(color, colors=set()):
    for content_color in content_to_container_mapping.get(color, []):
        colors.add(content_color)
        colors |= get_nr_bag_colors(content_color, colors)
    return colors

nr_colors = len(get_nr_bag_colors(BAG_COLOR))
print("PART 1 - Number of different bag colors that can contain at least one %s bag : %d" % (BAG_COLOR, nr_colors))

# PART 2
def get_nr_required_bags(color):
    nr_required_bags = 0
    for bag_color, quantity in container_to_content_mapping[color].items():
        nr_required_bags += quantity*(get_nr_required_bags(bag_color)+1)
    return nr_required_bags

print("PART 2 - Number of bags required inside a %s bag : %d" % (BAG_COLOR, get_nr_required_bags(BAG_COLOR)))
