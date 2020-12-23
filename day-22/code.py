with open("input.txt", "r") as file:
    player1, player2 = file.read().split("\n\n")

from collections import deque

player1 = deque(player1.split("\n")[1:])
player2 = deque(player2.split("\n")[1:])

while player1 and player2:
    v1, v2 = int(player1.popleft()), int(player2.popleft())
    if v1 > v2:
        player1.append(v1)
        player1.append(v2)
    else:
        player2.append(v2)
        player2.append(v1)

def compute_score(queue, N):
    s = 0
    while queue:
        s += queue.popleft()*N
        N -= 1
    return s

queue = player1 if player1 else player2
print(compute_score(queue, len(queue)))