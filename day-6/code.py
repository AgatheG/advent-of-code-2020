with open("input.txt", "r") as file:
    groups = file.read().split("\n\n")

# PART 1
count = 0
for group in groups:
    character_set = set(group)
    character_set.discard("\n")
    count += len(character_set)
print("PART 1 - Sum of the number of questions to which someone in a group answered yes : " + str(count))

# PART 2
count = 0
for group in groups:
    character_set = set()
    for idx, individual_answer in enumerate(group.split("\n")):
        if idx == 0:
            character_set |= set(individual_answer)
        else:
            character_set &= set(individual_answer)
    count += len(character_set)
print("PART 2 - Sum of the number of questions to which everyone in a group answered yes : " + str(count))