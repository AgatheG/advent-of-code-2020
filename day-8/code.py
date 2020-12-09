with open("input.txt", "r") as file:
    instructions = file.read().split("\n")

class Accumulator(object):
    def __init__(self):
        self.value = 0
        self.memory = 0

    def reset(self):
        self.value = self.memory
        self.memory = 0

    def add(self, offset):
        self.value += offset

    def store(self):
        self.memory = self.value

class Pointer(object):
    def __init__(self):
        self.acc = Accumulator()
        self.visited = set()
        self.memory = None
        super(Pointer, self).__init__()

    @property
    def value(self):
        return self.acc.value

    def add(self, offset):
        self.visited.add(self.value)
        self.acc.add(offset)

    def reset(self):
        self.visited = self.memory
        self.acc.reset()

    def clear_memory(self):
        self.memory = None

    def store(self):
        self.acc.store()
        self.memory = set(self.visited)

class InstructionReader(object):
    class OPERATIONS:
        Accumulator = "acc"
        Jump = "jmp"
        NoOperation = "nop"

    def __init__(self, instructions):
        self.idx = 0
        self.instructions = instructions
        self.pointer = Pointer()
        self.accumulator = Accumulator()

    def get_operation(self, code, argument):
        if code == self.OPERATIONS.Accumulator:
            self.accumulator.add(argument)
            self.pointer.add(1)
        if code == self.OPERATIONS.Jump:
            self.pointer.add(argument)
        if code == self.OPERATIONS.NoOperation:
            self.pointer.add(1)

    def reset(self):
        self.accumulator.reset()
        self.pointer.reset()

    def read_instruction(self):
        code, argument = self.instructions[self.pointer.value].split(" ")
        self.get_operation(code, int(argument))

    def is_looping(self):
        return self.pointer.value in self.pointer.visited

    def is_done(self):
        return self.pointer.value >= len(self.instructions)

reader = InstructionReader(instructions)

# PART 1
while not reader.is_looping():
    reader.read_instruction()

print("PART 1 - The accumulator value is : " + str(reader.accumulator.value))

# PART 2

class CorruptedInstructionReader(InstructionReader):
    CORRUPTIBLE_OP_CODES = {
        "jmp": "nop",
        "nop": "jmp"
    }

    def instruction_can_be_corrupted(self, code, argument):
        return code in self.CORRUPTIBLE_OP_CODES and argument != 0

    def no_repair_attempt_ungoing(self):
        return self.pointer.memory is None

    def get_operation(self, code, argument):
        if self.instruction_can_be_corrupted(code, argument) and self.no_repair_attempt_ungoing():
            self.pointer.store()
            self.accumulator.store()
            code = self.CORRUPTIBLE_OP_CODES[code]
        super(CorruptedInstructionReader, self).get_operation(code, argument)

reader = CorruptedInstructionReader(instructions)
while not reader.is_done():
    reader.read_instruction()
    if reader.is_looping():
        reader.reset()
        reader.read_instruction()
        reader.pointer.clear_memory()

print("PART 2 - The accumulator value is : " + str(reader.accumulator.value))
