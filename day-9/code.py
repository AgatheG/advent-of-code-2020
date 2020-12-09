from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")
parser.add_argument(
    "-p", "-preambule", type=int, default=25, dest="preambule_size")

args = parser.parse_args()

PREAMBLE_SIZE = args.preambule_size
with open(args.file, "r") as file:
    numbers = file.read().split("\n")

for i in range(len(numbers)):
    tested_number = int(numbers[i+PREAMBLE_SIZE])
    s, valid = set(), False
    for j in range(PREAMBLE_SIZE):
        number = int(numbers[i+j])
        if number in s:
            valid = True
            break
        s.add(tested_number - number)
    if not valid:
        break

print("PART 1 - The first invalid number is : " + str(tested_number))

#PART 2
from collections import deque

contiguous_set, accumulated_sum = deque(), 0
for number in numbers:
    number = int(number)
    if number > tested_number:
        contiguous_set, accumulated_sum = deque(), 0
    else:
        accumulated_sum += number
        contiguous_set.append(number)
        while accumulated_sum > tested_number:
            leftmost_term = contiguous_set.popleft()
            accumulated_sum -= leftmost_term
        if accumulated_sum == tested_number:
            break

print("PART 2 - The sum of the min and max of the coniguous set is worth : " + str(min(contiguous_set) + max(contiguous_set)))
