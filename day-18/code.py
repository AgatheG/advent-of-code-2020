with open("input.txt", "r") as file:
    lines = file.read().split("\n")

from collections import deque
import re

OPENING_PARENTHESES = "([\(]+)(\d)"
CLOSING_PARENTHESES = "(\d)([\)]+)"

def res_line(line):
    queue, op_queue = deque(), deque()
    for char in line:
        open_parentheses = re.search(OPENING_PARENTHESES, char)
        if open_parentheses is not None:
            parentheses, number = open_parentheses.groups()
            for i in range(len(parentheses) - 1):
                queue.appendleft(None)
            queue.appendleft(int(number))
            continue
        closing_parentheses = re.search(CLOSING_PARENTHESES, char)
        if closing_parentheses is not None:
            number, parentheses = closing_parentheses.groups()
            number = int(number)
            operator, other_number = op_queue.popleft(), queue.popleft()
            res = other_number + number if operator == "+" else other_number * number
            for i in range(len(parentheses)):
                if op_queue:
                    other_number = queue.popleft()
                    if other_number is not None:
                        operator = op_queue.popleft()
                        res = other_number + res if operator == "+" else other_number * res
            queue.appendleft(res)
        elif char.isdigit():
            number = int(char)
            if op_queue:
                operator, other_number = op_queue.popleft(), queue.popleft()
                queue.appendleft(other_number + number if operator == "+" else other_number * number)
            else:
                queue.appendleft(number)
        elif char == "+" or char == "*":
            op_queue.appendleft(char)
    return queue.popleft()

s = 0
for line in lines:
    s+=res_line(line.split(" "))
print(s)
