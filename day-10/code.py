from argparse import ArgumentParser
from heapq import heappush, heappop

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")

args = parser.parse_args()

with open(args.file, "r") as file:
    numbers = file.read().split("\n")

heap = []
for unparsed_number in numbers:
    heappush(heap, int(unparsed_number))

previous_joltage, sequential_one_diffs = 0, [0]
ones, threes = 0, 0

while heap:
    joltage = heappop(heap)
    diff = joltage - previous_joltage
    if diff == 1:
        ones += 1
        sequential_one_diffs[-1] += 1
    if diff == 3:
        threes += 1
        sequential_one_diffs.append(0)
    previous_joltage = joltage

#PART 1
print("PART 1 - The product is worth : " + str((threes+1) * ones))

#PART 2
def get_nr_combinations(n):
    res = pow(2, n)
    if n > 2:
        res += 1 - pow(2, n-2)
    return res

nr_combinations = 1
for nr_diffs in sequential_one_diffs:
    if nr_diffs > 1:
        nr_combinations *= get_nr_combinations(nr_diffs-1)

print("PART 2 - The number of combinations is : " + str(nr_combinations))
