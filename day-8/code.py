with open("input.txt", "r") as file:
    instructions = file.read().split("\n")

accumulator = [0]

def accumulator_operation(argument, idx):
    accumulator[0] += argument
    return idx+1

OPERATIONS = {
    "acc": accumulator_operation,
    "jmp": lambda argument, idx: argument+idx,
    "nop": lambda argument, idx: idx+1
}

# PART 1

instruction_idx, visited_ids = 0, set()
while instruction_idx not in visited_ids:
    visited_ids.add(instruction_idx)
    operation, argument = instructions[instruction_idx].split(" ")
    prev = instruction_idx
    instruction_idx = OPERATIONS[operation](int(argument), instruction_idx)
print(accumulator)

# PART 2
CORRUPTIBLE_OPS = ["jmp", "nop"]
go_back = [0]
accumulator = [0]
d = {}

def is_potentially_corrupted(operation, argument, idx):
    return idx not in tried_ids and idx in new_visited_ids and go_back[0] == -1 and argument != 0 and operation in CORRUPTIBLE_OPS

def changed_operation(operation, argument, idx):
    if is_potentially_corrupted(operation, argument, idx):
        go_back[0] = idx
        tried_ids.add(idx)
        changed_operation = "nop" if operation == "jmp" else "jmp"
        return OPERATIONS[changed_operation](argument, idx) 
    return OPERATIONS[operation](argument, idx)

tried_ids = set()
instruction_idx, new_visited_ids = 0, set()
while instruction_idx < len(instructions):
    if instruction_idx not in d and instruction_idx in visited_ids:
        d[instruction_idx] = {
            "set": set(new_visited_ids),
            "acc": accumulator[0]
        }
    new_visited_ids.add(instruction_idx)
    operation, argument = instructions[instruction_idx].split(" ")
    instruction_idx = changed_operation(operation, int(argument), instruction_idx)

    if instruction_idx in new_visited_ids:
        instruction_idx = go_back[0]
        new_visited_ids = set(d[instruction_idx]["set"])
        accumulator = [d[instruction_idx]["acc"]]
        go_back[0] = -1

print(accumulator)