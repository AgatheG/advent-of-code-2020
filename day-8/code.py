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
        self.clear_memory()

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

    class FIX_ATTEMPT:
        NoneOngoing = 0
        Ongoing = 1
        Failed = 2
        
    def __init__(self, instructions):
        self.fix_attempt = self.FIX_ATTEMPT.NoneOngoing
        super(CorruptedInstructionReader, self).__init__(instructions)

    def reset(self):
        self.fix_attempt = self.FIX_ATTEMPT.Failed
        super(CorruptedInstructionReader, self).reset()

    def can_attempt_instruction_fix(self, code, argument):
        corruptible_instruction = code in self.CORRUPTIBLE_OP_CODES and argument != 0
        return corruptible_instruction and self.fix_attempt == self.FIX_ATTEMPT.NoneOngoing

    def start_fix_attempt(self):
        self.pointer.store()
        self.accumulator.store()
        self.fix_attempt = self.FIX_ATTEMPT.Ongoing

    def get_operation(self, code, argument):
        if self.can_attempt_instruction_fix(code, argument):
            self.start_fix_attempt()
            code = self.CORRUPTIBLE_OP_CODES[code]
        if self.fix_attempt == self.FIX_ATTEMPT.Failed:
            self.fix_attempt = self.FIX_ATTEMPT.NoneOngoing
        super(CorruptedInstructionReader, self).get_operation(code, argument)

reader = CorruptedInstructionReader(instructions)
while not reader.is_done():
    reader.read_instruction()
    if reader.is_looping():
        reader.reset()

print("PART 2 - The accumulator value is : " + str(reader.accumulator.value))
