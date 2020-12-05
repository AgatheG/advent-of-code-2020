with open("input.txt", "r") as file:
    lines = file.read().split("\n")

def translate_to_decimal(string, zero_char, one_char):
    return int(string.replace(zero_char, "0").replace(one_char, "1"), 2)

def get_seat_id(line):
    row, col = translate_to_decimal(line[:-3], "F", "B"), translate_to_decimal(line[-3:], "L", "R")
    return 8*row + col

THEORITICAL_HIGHEST_SEAT_ID = 127*8+7

taken_ids = [0]*THEORITICAL_HIGHEST_SEAT_ID
highest_seat_id, lowest_seat_id = 0, THEORITICAL_HIGHEST_SEAT_ID

for line in lines:
    seat_id = get_seat_id(line)
    taken_ids[seat_id] = 1
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    if seat_id < lowest_seat_id:
        lowest_seat_id = seat_id

print("PART 1 - The highest seat id is : " + str(highest_seat_id))
print("PART 2 - The seat id is : " + str(taken_ids[lowest_seat_id:].index(0) + lowest_seat_id))
