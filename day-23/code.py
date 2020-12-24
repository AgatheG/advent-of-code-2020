input_data = "586439172"
N = 9

# INIT
    


def pick_up_cups(current_idx, input_data):
    s = ""
    new_data = input_data
    for i in range(1,4):
        char = input_data[(current_idx+i)%N]
        s += char
        new_data = new_data.replace(char, "")
    return s, new_data

def find_destination(current_cup, picked_up_cups, input_data):
    destination_label = str(int(current_cup) - 1)
    while destination_label != "0" and destination_label in picked_up_cups:
        destination_label = str(int(destination_label)-1)
    if destination_label == "0":
        return sorted(input_data)[-1]
    return destination_label

current_idx = 0
for turn in range(100):
    current_cup = input_data[current_idx%N]
    picked_up_cups, input_data = pick_up_cups(current_idx, input_data)
    destination = find_destination(current_cup, picked_up_cups, input_data)
    input_data = input_data.replace(destination, destination + picked_up_cups)
    current_idx = input_data.index(current_cup)+1

print(input_data)
