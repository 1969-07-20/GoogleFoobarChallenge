""" This file implements a solution to the 'Bringing a Gun to a Guard Fight'
    puzzle.

Description of algorithm
     The following observations are key to this solution to the Bringing a Gun
     to a Guard Fight puzzle:

    1) There is a conceptual model in optics that the path of a beam of light
       reflecting off a surface travels along a path as if the space on one
       side of the surface were mirror reflected about that surface and the
       light continued straight in the reflected space.

       If the light continues far enough to reflect off another surface, its
       path is the same as if the reflected space were mirror reflected again
       across that surface and the light continued propagating in the doubly
       reflected space.

       By repeated mirror reflection, one can tile space for an indefinite
       distance in any direction.  The term "tile" is used extensively in this
       solution.  The term refers to a particular translated and reflected copy
       of the room in the tiling of 2-space mentioned at the beginning of the
       paragraph.

    2) To shoot a guard via a path that bounces off mirror(s) one or more times,
       all that is needed is to aim at the guard's reflected image in one of
       the tiles.  The distance to the guard's image in that tile is the
       distance the beam will travel bouncing around the room.  This makes
       it very easy to determine whether or not the beam will be strong
       enough to do damage when it reaches the guard traveling along that path.

       Just as the guard gets reflected in the tiles, so do ourselves.  It is
       possible that a reflected image ourselves lies on the same bearing. If
       the closest image of ourselves lies at a smaller distance than the
       closest image of the guard, then we will be hit by the beam before the
       guard, obviously something to be avoided.

    3) The vertical and horizontal reflection operations are commutative. The
       order of horizontal and vertical reflections does not matter.  Therefore,
       to determine whether x coordinates in a reflected tile are the same or
       reversed relative to the original, unreflected tile, one only needs to
       know if an even or odd number of reflections about vertical mirrors
       have taken place.

       Similarly, to determine whether y coordinates in a reflected tile are the
       same or reversed relative to the original, unreflected tile, one only
       needs to know if an even or odd number of reflections about horizontal
       mirrors have taken place.

       The repeated reflections creates an infinite repeating pattern of
       reflected images of the original space.  The following is a portion
       of the pattern.

       - A "(++)" denotes a tile that is identical to the original space.
       - A "(-+)" denotes a tile reflected about a vertical axis.
       - A "(+-)" denotes a tile reflected about a horizontal axis.
       - A "(--)" denotes a tile reflected about both horiz and vert axes.

       (++) (-+) (++) (-+) (++)
       (+-) (--) (+-) (--) (+-)
       (++) (-+) (++) (-+) (++)
       (+-) (--) (+-) (--) (+-)
       (++) (-+) (++) (-+) (++)

       - For (++) tiles, (x',y') = (x,y)
       - For (-+) tiles, (x',y') = (-x,y)
       - For (+-) tiles, (x',y') = (x,-y)
       - For (--) tiles, (x',y') = (-x,-y)

    This solution's strategy is quite simple.  It operates in two phases. In the
    first phase, the solution creates two Python dictionaries.  One dictionary
    has the bearings and distances of all the reflected image of the guard in
    tiles where the guard's distance is less than or equal to the maximum
    beam distance.  This is the "target" dictionary.  It is possible that
    multiple reflected images of the guard lie on the same bearing.  Only the
    closest image of the guard is recorded.  The second dictionary does the same
    for ourselves.  This is the "exclude" dictionary.

    The key used for each entry in the dictionaries is a textual encoding of the
    vector representation of the bearing.  In the second phase of the solution,
    a pass is made through the keys of the target dictionary.  If there is an
    entry in the exclude dictionary for that key then there is a reflected image
    of ourselves on the same bearing.  The dictionary records the minimum
    distance to an image along that bearing.  If the distance is less in the
    target dictionary than the distance in the exclude dictionary, we know that
    the guard will be hit and the count of viable bearings is incremented for
    that bearing.  If there is no entry in the exclude dictionary for that key,
    we know that there is no reflected image of ourselves along that bearing and
    the count is also incremented in this case.

    At the end of the single pass through the keys in the target dictionary, we
    know how many viable bearings there are to shoot and hit the guard without
    shooting ourselves.

    The keys in the dictionaries encode the bearing via concatenating the x
    component of the vector representation of the bearing and the y component,
    separated by ":".  Since our position as well as the guard's positions are
    on an integer lattice, the bearings are rational numbers.  The x and y
    components are the denominator and numerator of the rational number after
    being reduced to lowest terms.  Signs of the components are preserved to
    distinguish between pairs of opposite bearings.

Time and space complexity of the solution:

    If 'dist' is the maximum distance of the beam and 'dim_x' and 'dim_y' are
    the x and y dimensions of the room, define M = dist / dim_x and
    N = dist / dim_y.  The solution has O(M * N) = O((dist^2 / (dim_x * dim_y))
    time and space complexity.  The following is the reasoning behind this
    claim.

    The time and space complexities are proportional to the number of dictionary
    entries.  The time and space complexity to create a dictionary entry in the
    first phase or to process an entry in the second phase is O(1).  This code's
    time and space complexity to process a tile is O(1) and in the average case
    the same is true for Python dictionary get and set operations.  See
    https://wiki.python.org/moin/TimeComplexity.

    The number of dictionary entries is upper bounded by the number
    of tiles that overlap a circle of radius dist which is O(dist^2) area.
    The area of a tile is dim_x * dim_y so the number of tiles is about the
    area of the circle divided by the area of a tile or
    O(dist^2 / (dim_x * dim_y)) = O(M * N).

Assumptions/restrictions:
    None beyond the limitations stated in the problem statement.

This solution is completely of my own conception and execution.
"""

from math import sqrt
from fractions import gcd


def calc_reflected_pos(x0, y0, tile_x, tile_y, dim_x, dim_y):
    """Compute the coordinates of the point in tile (tile_x, tile_y)
    corresponding to the point (x0,y0) in original, unreflected tile/room."""


    #  Calculate x coordinate of reflected image
    if (tile_x % 2) == 0:
        x = tile_x * dim_x + x0
    else:
        x = (tile_x + 1) * dim_x - x0


    #  Calculate y coordinate of reflected image
    if (tile_y % 2) == 0:
        y = tile_y * dim_y + y0
    else:
        y = (tile_y + 1) * dim_y - y0


    #  Return coordinates of reflected image
    return x, y


def process_bearing(x0, y0, x, y):
    """Compute the x and y components of bearing from me to guard; return in
    form of numerator and denominator of a reduced fraction."""


    #  Handle special case of both x0 = x and y0 = y
    if (x0 == x) and (y0 == y):
        return (0, 0)


    #  Calculate x and y components of bearing
    bear_x = x - x0
    bear_y = y - y0


    #  Separate x and y components into sign and magnitude
    if bear_x >= 0:
        sign_x = 1
    else:
        sign_x = -1

    bear_x = abs(bear_x)


    if bear_y >= 0:
        sign_y = 1
    else:
        sign_y = -1

    bear_y = abs(bear_y)


    #  Reduce vector representation of bearing to lowest terms
    if bear_y == 0:  # Horizontal line requires special handling
        bear_x = 1
    elif bear_x == 0:  # Vertical line requires special handling
        bear_y = 1
    else:

        #  Remove common factors from bearing components
        greatest_common_factor = gcd(bear_x, bear_y)

        if greatest_common_factor != 1:
            bear_x //= greatest_common_factor
            bear_y //= greatest_common_factor


    #  Restore signs of x and y components
    bear_x *= sign_x
    bear_y *= sign_y


    #  Return bearing components
    return bear_x, bear_y


def process_image(x, y, my_x0, my_y0, max_distance, dictionary):
    """Update dictionary with information about this reflected image."""


    #  Calculate distance to image in this tile
    dist = sqrt((x - my_x0) ** 2 + (y - my_y0) ** 2)


    #  Skip this tile if distance to reflected image
    #  exceeds max beam distance OR the distance is 0
    if (dist <= max_distance) and (dist > 0):


        #  Get bearing from me to reflected image
        bear_x, bear_y = process_bearing(my_x0, my_y0, x, y)


        #  Encode bearing into dictionary key
        key_str = "%+06d:%+06d" % (bear_x, bear_y)


        #  Store info about this reflected image as appropriate
        if key_str in dictionary:
            if dist < dictionary[key_str]:
                dictionary[key_str] = dist
        else:
            dictionary[key_str] = dist


def get_bearing_info(room_dims, my_position, guard_position, max_distance):
    """Create dictionaries with the bearings of all reflected images of the
    guard and ourselves less than the maximum distance of the beam away."""


    #  Make local copies of my and guard's actual positions
    guard_x0 = guard_position[0]
    guard_y0 = guard_position[1]

    my_x0 = my_position[0]
    my_y0 = my_position[1]


    #  Make local copy of room's dimensions
    dim_x = room_dims[0]
    dim_y = room_dims[1]


    #  Calculate maximum number of tiles horizontally and vertically the beam
    #  can travel
    m_max = max_distance // dim_x
    n_max = max_distance // dim_y

    m_min = -m_max
    n_min = -n_max

    while max_distance > ((guard_x0 + m_max * dim_x) - my_x0):
        m_max += 1

    while max_distance > ((guard_y0 + n_max * dim_y) - my_y0):
        n_max += 1

    while max_distance > (my_x0 - (guard_x0 + m_min * dim_x)):
        m_min -= 1

    while max_distance > (my_y0 - (guard_y0 + n_min * dim_y)):
        n_min -= 1


    #  Create blank dictionaries to hold target and exclude bearings
    target_bearings = {}
    exclude_bearings = {}


    #  Loop over tiles from bottom to top
    for tile_y in range(n_min, n_max + 1):

        #  Loop over tiles from left to right
        for tile_x in range(m_min, m_max + 1):

            #  Get positions of reflected images of guard and me in tile
            guard_x, guard_y = calc_reflected_pos(
                guard_x0, guard_y0, tile_x, tile_y, dim_x, dim_y)

            my_x, my_y = calc_reflected_pos(
                my_x0, my_y0, tile_x, tile_y, dim_x, dim_y)


            #  Update dictionaries with info about reflected images in this tile
            process_image(guard_x, guard_y, my_x0, my_y0, max_distance, target_bearings)
            process_image(my_x, my_y, my_x0, my_y0, max_distance, exclude_bearings)


    #  Return info about bearings to guard's and my reflected images
    return target_bearings, exclude_bearings


def count_viable_bearings(target_bearings, exclude_bearings):
    """Using the dictionaries for the guard and ourselves, count the number of
    bearings we can shoot the guard without shooting ourselves."""


    bearing_count = 0


    #  Loop over bearings in target dictionary (encoded in dictionary keys)
    for target_key in target_bearings.keys():

        #  If there is no corresponding entry in exclude dictionary, it's a hit
        if not target_key in exclude_bearings:
            bearing_count += 1

        #  If the same bearings is in exclude_bearings, this is a hit if distance to
        #  guard is less than distance to me.  Otherwise it's a miss.
        elif target_bearings[target_key] < exclude_bearings[target_key]:
                bearing_count += 1


    #  Return number of viable bearings
    return bearing_count


def solution(room_dims, my_position, guard_position, max_distance):
    """Solve the Bringing a Gun to a Guard Fight puzzle and return the answer."""


    #  Get info about reflected images of guard and myself
    target_bearings, exclude_bearings = get_bearing_info (room_dims,
        my_position, guard_position, max_distance)


    #  Using the info about reflected images, count number of viable bearings
    bearing_count = count_viable_bearings(target_bearings, exclude_bearings)


    #  Return number of viable bearings to shoot guard
    return bearing_count



# print (solution([3,2], [1,1], [2,1], 4))
# print (solution([300,275], [150,150], [185,100], 500))
