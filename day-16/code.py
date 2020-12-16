import re
from heapq import heappush, heappop

with open("input.txt", "r") as file:
    fields, own_ticket, nearby_tickets = file.read().split("\n\n")

# INIT

FIELD_PATTERN = "^([a-z\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$"
field_dict = {}
for field in fields.split("\n"):
    matching_groups = re.match(FIELD_PATTERN, field).groups()
    field_dict[matching_groups[0]] = [int(bound) for bound in matching_groups[1:]]

nearby_tickets = nearby_tickets.split("\n")[1:]

own_ticket = own_ticket.split("\n")[1].split(",")

# PART 1

scanning_error_rate = 0
valid_tickets = [] # for part 2
for ticket in nearby_tickets:
    kept_ticket = []
    for field in ticket.split(","):
        field, is_valid = int(field), False
        for lb1, ub1, lb2, ub2 in field_dict.values():
            if lb1 <= field <= ub1 or lb2 <= field <= ub2:
                is_valid = True
                break
        if is_valid:
            kept_ticket.append(field)
        else:
            scanning_error_rate += field
    if len(kept_ticket) == len(field_dict):
        valid_tickets.append(kept_ticket)

print("PART 1 - Scanning error rate is : " + str(scanning_error_rate))

# PART 2

heap = []
for idx in range(len(field_dict)):
    possible_fields = set(field_dict.keys())
    for ticket in valid_tickets:
        field = ticket[idx]
        valid_fields = set()
        for field_name in field_dict:
            lb1, ub1, lb2, ub2 = field_dict[field_name]
            if lb1 <= field <= ub1 or lb2 <= field <= ub2:
                valid_fields.add(field_name)
        possible_fields &= valid_fields
    heappush(heap, (len(possible_fields), idx, possible_fields))

not_found_fields = set(field_dict.keys())
remaining_fields_to_find = set(field for field in field_dict.keys() if field.startswith("departure"))
product = 1
while remaining_fields_to_find:
    _, idx, possible_values = heappop(heap)
    possible_values &= not_found_fields
    field = possible_values.pop()
    not_found_fields.remove(field)
    if field in remaining_fields_to_find:
        product *= int(own_ticket[idx])
        remaining_fields_to_find.remove(field)

print("PART 2 : " + str(product))
    