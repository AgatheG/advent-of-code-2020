import re

with open("input.txt", "r") as file:
    lines = file.read().split("\n")

MASK_PATTERN = "^mask\s=\s([0-9X]{36})$"
MEM_PATTERN = "^mem\[(\d+)\]\s=\s(\d+)$"

def get_padded_binary(num):
    return format(num, "036b")

# PART 1

def write_masked_value(value, mask, address):
    bin_value = get_padded_binary(value)
    masked_value = ""
    for idx, bit in enumerate(bin_value):
        masked_value += bit if mask[idx] == "X" else mask[idx]
    mem[address] = int(masked_value, 2)

mem = {}

for line in lines:
    mask_groups = re.search(MASK_PATTERN, line)
    if mask_groups is not None:
        mask = mask_groups.group(1)
    else:
        address, value = re.search(MEM_PATTERN, line).groups()
        write_masked_value(int(value), mask, address)

print("PART 1", sum(v for v in mem.values()))

# PART 2

def write_to_masked_address(address, mask, value, masked_address=""):
    if len(masked_address) == len(mask):
        mem[int(masked_address, 2)] = value
        return
    offset = len(masked_address)
    if mask[offset] == "0":
        write_to_masked_address(address, mask, value, masked_address + address[offset])
    if mask[offset] == "1":
        write_to_masked_address(address, mask, value, masked_address + mask[offset])
    if mask[offset] == "X":
        write_to_masked_address(address, mask, value, masked_address + "0")
        write_to_masked_address(address, mask, value, masked_address + "1")

mem = {}
for line in lines:
    mask_groups = re.search(MASK_PATTERN, line)
    if mask_groups is not None:
        mask = mask_groups.group(1)
    else:
        address, value = re.search(MEM_PATTERN, line).groups()
        write_to_masked_address(get_padded_binary(int(address)), mask, int(value))

print("PART 2", sum(v for v in mem.values()))
