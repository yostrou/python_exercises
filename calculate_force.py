from math import atan2, degrees, radians, sin, cos

# Write a function called find_net_force. find_net_force should
# have one parameter: a list of instances of Force. The
# function should return new instance of Force with the total
# net magnitude and net angle as the values for its magnitude
# and angle attributes.


class Force:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    def get_horizontal(self):
        return self.magnitude * cos(self.get_angle(use_degrees=False))

    def get_vertical(self):
        return self.magnitude * sin(self.get_angle(use_degrees=False))

    def get_angle(self, use_degrees=True):
        if not use_degrees:
            return radians(self.angle)
        else:
            return self.angle


def find_net_force(forces):
    """
    Calculate the net force from a list of forces
    """
    total_horizontal = 0
    total_vertical = 0
    for force in forces:
        total_horizontal += force.get_horizontal()
        total_vertical += force.get_vertical()

    net_magnitude = (total_horizontal ** 2 + total_vertical ** 2) ** 0.5
    net_magnitude = round(net_magnitude, 1)
    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = round(degrees(net_angle), 1)

    return Force(net_magnitude, net_angle)


force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)  # 103.1
print(net_force.angle)  # -14.0
