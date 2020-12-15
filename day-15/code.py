input_numbers = [9,19,1,6,0,5,4]

def find_number(N):
    d = {}
    for i in range(N):
        if i < len(input_numbers):
            value = int(input_numbers[i])
            d[value] = (i, True)
            previous = value
        else:
            value, first_time = d.get(previous, (-1, True))
            if first_time:
                previous = 0
            else:
                d[previous] = (i-1, False)
                previous = i-1-value
            d[previous] = (d.get(previous, [i])[0], previous  not in d)
    return previous

print("PART 1", find_number(2020))
print("PART 2", find_number(30000000)) # bit ugly (approx. 30sec)
