import re
with open("input.txt", "r") as file:
    lines = file.read().split("\n")

MATCHING_PATTERN = "^(\d*)-(\d*)\s(\w):\s(\w*)$"

# PART 1
valid_passwords = 0
for line in lines:
    lower_bound, upper_bound, letter, password = re.search(MATCHING_PATTERN, line).groups()
    if int(lower_bound) <= password.count(letter) <= int(upper_bound):
        valid_passwords += 1

print("PART 1 - The number of valid passwords is " + str(valid_passwords))

#PART 2
valid_passwords = 0
for line in lines:
    index_1, index_2, letter, password = re.search(MATCHING_PATTERN, line).groups()
    index_1, index_2 = int(index_1) - 1, int(index_2) - 1
    letter_at_idx_1 = index_1 < len(password) and password[index_1] == letter
    letter_at_idx_2 = index_2 < len(password) and password[index_2] == letter
    if letter_at_idx_1:
        if not letter_at_idx_2:
            valid_passwords += 1
    elif letter_at_idx_2:
        valid_passwords += 1

print("PART 2 - The number of valid passwords is " + str(valid_passwords))
