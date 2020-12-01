with open("input.txt", "r") as file:
    expenses = file.read().split("\n")

SUM_VALUE = 2020

# PART 1
s = set()
def get_sum_components():
    for expense_1 in expenses:
        expense_1 = int(expense_1)
        expense_2 = SUM_VALUE - expense_1
        if expense_1 in s:
            return expense_1, expense_2
        s.add(expense_2)

expense_1, expense_2 = get_sum_components()
print("PART 1 - Product of the expenses is worth " + str(expense_1 * expense_2))

# PART 2
def get_sum_components():
    for i, expense_1 in enumerate(expenses):
        expense_1, s = int(expense_1), set()

        for j in range(i, len(expenses)):
            expense_2 = int(expenses[j])
            expense_3 = SUM_VALUE - expense_1 - expense_2
            if expense_2 in s:
                return expense_1, expense_2, expense_3
            s.add(expense_3)

expense_1, expense_2, expense_3 = get_sum_components()
print("PART 2 - Product of the expenses is worth " + str(expense_1 * expense_2 * expense_3))
