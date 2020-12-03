with open("input.txt", "r") as file:
    lines = file.read().split("\n")

TREE_PATTERN = "#"

def tree_check(line, slope):
    return line[slope%len(line)] == TREE_PATTERN

#PART 1
encountered_trees = 0

for idx, line in enumerate(lines):
    if tree_check(line, 3*idx):
        encountered_trees+=1

print("PART 1 - Number of trees encountered following this slope : " + str(encountered_trees))

# PART 2
encountered_trees = {
    1: 0,
    3: encountered_trees,
    5: 0,
    7: 0,
    .5: 0
}
for idx, line in enumerate(lines):
    if tree_check(line, idx):
        encountered_trees[1] += 1
    if tree_check(line, 5*idx):
        encountered_trees[5] += 1
    if tree_check(line, 7*idx):
        encountered_trees[7] += 1
    if idx%2==0 and tree_check(line, idx/2):
        encountered_trees[.5] += 1

print("PART 2 - Multiplying the number of trees encountered for these five differents slopes yields : " 
    + str(reduce(lambda x, y: x*y, encountered_trees.values())))
