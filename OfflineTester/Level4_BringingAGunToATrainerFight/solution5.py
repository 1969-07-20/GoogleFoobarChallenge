'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/wrbyepct/Bringing-a-gun-to-a-trainer-fight/blob/master/solution/solution_revised.py"


from math import sqrt, ceil, atan2

"""
Upperbound finder
"""


def get_upperbound_len(your_position, radius, room_size):
    return int(ceil((your_position[0] + radius) / room_size[0]))


def get_upperbound_wid(your_position, radius, room_size):
    return int(ceil((your_position[1] + radius) / room_size[1]))


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def angle(p1, p2):
    return atan2((p2[1] - p1[1]), (p2[0] - p1[0]))


def solution(room_size, me_position, trainer_position, radius):
    # Find all possible points in the first quadrant
    # Radius / dimension -> The radius is roughly how many times of the length/height of the room
    times_len = get_upperbound_len(me_position, radius, room_size)
    times_wid = get_upperbound_wid(me_position, radius, room_size)
    # Create mirrored room
    me_mirror_x = - me_position[0] + room_size[0]
    me_mirror_y = - me_position[1] + room_size[1]
    trainer_mirror_x = - trainer_position[0] + room_size[0]
    trainer_mirror_y = - trainer_position[1] + room_size[1]
    q1_me = []
    q1_target = []
    for i in range(0, times_len + 1):
        for j in range(0, times_wid + 1):
            me_x = me_mirror_x + i * room_size[0] if i % 2 != 0 else me_position[0] + i * room_size[0]
            me_y = me_mirror_y + j * room_size[1] if j % 2 != 0 else me_position[1] + j * room_size[1]
            temp_me = [me_x, me_y]
            trainer_x = trainer_mirror_x + i * room_size[0] if i % 2 != 0 else trainer_position[0] + i * room_size[
                0]
            trainer_y = trainer_mirror_y + j * room_size[1] if j % 2 != 0 else trainer_position[1] + j * room_size[
                1]
            temp_trainer = [trainer_x, trainer_y]
            q1_me.append(temp_me)
            q1_target.append(temp_trainer)

    # generate all possible all_points in q2, q3, and q4
    me_all_quadrants = q1_me + \
                       [[-x, y] for [x, y] in q1_me] +\
                       [[-x, -y] for [x, y] in q1_me] +\
                       [[x, -y] for [x, y] in q1_me]
    trainer_all_quadrants = q1_target + \
                            [[-x, y] for [x, y] in q1_target] +\
                            [[-x, -y] for [x, y] in q1_target] + \
                            [[x, -y] for [x, y] in q1_target]

    # Label each point with code and calculate the distance for later use
    me = [[distance(me_position, [x, y]), [x, y], 1] for [x, y] in me_all_quadrants]
    trainer = [[distance(me_position, [x, y]), [x, y], 2] for [x, y] in trainer_all_quadrants]
    corners = [[distance(me_position, [x, y]), [x, y], 3] for [x, y] in
               [(0, 0), (room_size[0], 0), (room_size[0], room_size[1]), (0, room_size[1])]]

    # Filter out the point out of range
    all_points = filter(lambda p: p[0] <= float(radius), me + trainer + corners)
    # Sort them with distance, because I can only hit the first one with same angle
    all_points = sorted(all_points, key=lambda p: p[0])

    # Angle dictionary, record the angle that have seen
    angles = {}
    # Skipping the first point, because it's our original points
    for point in all_points[1:]:
        # Record only the angle that has not been seen
        agl = angle(me_position, point[1])
        if agl not in angles:
            angles[agl] = point[2]
    # Count only the angle that's point at target
    return sum(1 for point_code in angles.values() if point_code == 2)
