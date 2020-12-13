with open("input.txt", "r") as file:
    timestamp, ids = file.read().split("\n")

timestamp, ids = int(timestamp), ids.split(",")
NO_BUS = "x"

# PART 1
bus_id_to_take, time_to_wait = None, timestamp
product = 1
for bus_id in ids:
    if bus_id != NO_BUS:
        bus_id = int(bus_id)
        product *= bus_id
        remaining_time = bus_id-timestamp%bus_id
        if remaining_time < time_to_wait:
            bus_id_to_take, time_to_wait = bus_id, remaining_time
print("PART 1", bus_id_to_take*time_to_wait)

#PART 2

def get_bezout_coef(a, b):
    if a == 0 :
        return 0,1
    x, y = get_bezout_coef(b%a, a)
    return y - x*(b/a), x

s = 0
for idx, bus_id in enumerate(ids):
    if idx != 0 and bus_id != NO_BUS:
        bus_id = int(bus_id)
        n = product/bus_id
        a, b = get_bezout_coef(n, bus_id)
        temp = (idx*a*n)
        s+= temp
print("PART 2", product - s%product)
