import re

with open("input.txt", "r") as file:
    lines = file.read().split("\n")

class Ship(object):
    directions = ["N", "E", "S", "W"]
    
    class Action:
        NORTH = "N"
        SOUTH = "S"
        WEST = "W"
        EAST = "E"
        FORWARD = "F"
        LEFT = "L"
        RIGHT = "R"

    def __init__(self):
        self.direction = self.Action.EAST
        self.x_dist = 0
        self.y_dist = 0
    
    def move(self, action, value):
        if action == self.Action.NORTH:
            self.y_dist += value
        elif action == self.Action.SOUTH:
            self.y_dist -= value
        elif action == self.Action.WEST:
            self.x_dist -= value
        elif action == self.Action.EAST:
            self.x_dist += value
        elif action == self.Action.FORWARD:
            self.move(self.direction, value)
        elif action == self.Action.LEFT:
            dir_idx = self.directions.index(self.direction)
            self.direction = self.directions[(dir_idx - value / 90) % 4]
        elif action == self.Action.RIGHT:
            dir_idx = self.directions.index(self.direction)
            self.direction = self.directions[(dir_idx + value / 90) % 4]

ship = Ship()
for line in lines:
    action, value = re.search("^([N|S|W|E|F|L|R])(\d+)$", line).groups()
    ship.move(action, int(value))

print(abs(ship.x_dist) + abs(ship.y_dist))

class ShipWithWaypoint(Ship):
    def __init__(self):
        self.waypoint = {Ship.Action.EAST: 10, Ship.Action.NORTH: 1}
        super(ShipWithWaypoint, self).__init__()

    def move_regarding_waypoint(self, action, value):
        if action == self.Action.NORTH:
            if self.Action.NORTH not in self.waypoint:
                self.waypoint[self.Action.SOUTH] -= value
            else:
                self.waypoint[self.Action.NORTH] += value
        elif action == self.Action.SOUTH:
            if self.Action.SOUTH not in self.waypoint:
                self.waypoint[self.Action.NORTH] -= value
            else:
                self.waypoint[self.Action.SOUTH] += value
        elif action == self.Action.WEST:
            if self.Action.WEST not in self.waypoint:
                self.waypoint[self.Action.EAST] -= value
            else:
                self.waypoint[self.Action.WEST] += value
        elif action == self.Action.EAST:
            if self.Action.EAST not in self.waypoint:
                self.waypoint[self.Action.WEST] -= value
            else:
                self.waypoint[self.Action.EAST] += value
        elif action == self.Action.FORWARD:
            for direction, w_value in self.waypoint.items():
                self.move(direction, value*w_value)
        elif action == self.Action.LEFT:
            directions = {}
            for direction, w_value in self.waypoint.items():
                dir_idx = self.directions.index(direction)
                w_direction = self.directions[(dir_idx - value / 90) % 4]
                directions[w_direction] = w_value
            self.waypoint = directions
        elif action == self.Action.RIGHT:
            directions = {}
            for direction, w_value in self.waypoint.items():
                dir_idx = self.directions.index(direction)
                w_direction = self.directions[(dir_idx + value / 90) % 4]
                directions[w_direction] = w_value
            self.waypoint = directions

ship = ShipWithWaypoint()
for line in lines:
    action, value = re.search("^([N|S|W|E|F|L|R])(\d+)$", line).groups()
    ship.move_regarding_waypoint(action, int(value))

print(abs(ship.x_dist) + abs(ship.y_dist))
