"""
The function solution(dimensions, my_position, trainer_position, max_distance)
computes solutions to the Bring a Gun to the Trainer Fight problem.  Given
'dimensions', a two element array with the X and Y dimensions of the room,
'my_position', 'trainer_position', the (x,y) coordinates of myself and the
trainer adversary, and 'max_distance' the maximum distance my laser gun can
shoot, solution() returns the number of distinct directions that I can shoot
the trainer without shooting myself.

Two aspects to the problem are key to the solution.  The first is that the
laser reflections behave as if a mirror image of the room were present on the
other side of the mirror and the laser traveled straight into that mirror
image.  Repeated reflections can be treated as if the room was mirror imaged
multiple times and the laser had traveled in straight line through them.  This
is a well-known mental model in optics as well as in billiards.

The second key to solving this challenge is the fact that the dimensions and
positions are all restricted to integer values.  As a result, the straight line
through the mirror images of the room mentioned in the previous paragraph can be
represented by a linear Diophantine equation in two variables.  The fact that it
is a linear Diophantine equation allows us to quickly determine if any solutions
exist.  And if a solution the Diophantine equation exists, we know an infinite
number of evenly spaced solutions exist.

This solution to the Bring a Gun to the Trainer Fight challenge relies on two
types of Diophantine equations.  The first is a simple linear equation in the
two position variables.  It is the equation for the line passing through my
position (x0,y0) and that of the replica of the trainer in one of the mirror
images of the room (x1,y1).  The laser beam follows this line and if my
position in any intermediate mirror image of the room lies on this line, the
laser will hit me before reaching the trainer I am aiming at.  The equation
for this line takes the form a*x + b*y = c.  The coefficients can be expressed
in terms of my position (x0,y0) and the trainer (x1,y1).

a = y1 - y0
b = x0 - x1
c = (y1 - y0) * x0 + (x0 - x1) * y0

The second type of Diophantine equation is a family of four related linear
Diophantine equations.  The variables in this family of equations are m and n.
The equations are also linear Diophantine equations and therefore have the form
a*m + b*n = c.  The different members of the family differ in the value of c.
This family of equations enables us to determine if any of my reflections lie
on the line passing through me and the replica of the trainer.  There is one
member of this family for each of the types of replicas of myself.

The locations of the replicas of each type of replica of myself are found by
negating one or both of the X and Y coordinates of my position.  If dim_x and
dom_y are the X and Y dimensions of the room, each type of replicas of myself
are separated from other replicas of the same type by m times twice dim_x in
the X dimension and n times twice dim_y in the Y dimension.  Expressed
mathematically, the location of each type of replica of myself is given by

(m * 2 * dim_x +- x0, n * 2 * dim_y +- y0)

or, expressed another, way at (x,y) such that

x = m * 2 * dim_x +- x0
y = n * 2 * dim_y +- y0

Substituting these expressions for x and y in the equation of the line through
me and the replica of the trainer, and simplifying gives a equations of the
form a*m + b*n = c where c is determined by the choice of sign on the x0 and y0
terms above.  These express the location of each type of replica of myself lying
on the line through myself and the replica of the trainer.

Once again the coefficients can be expressed in terms of x0, y0, x1, y1, dim_x and
dim_y:

a = (y1 - y0) * dim_x
b = (x0 - x1) * dim_y
c_pp = 0                                 (my replica at (x0,y0))
c_mp = (y1 - y0) * x0                    (my replica at (-x0,y0))
c_pm = (x0 - x1) * y0                    (my replica at (x0,-y0))
c_mm = (y1 - y0) * x0 + (x0 - x1) * y0   (my replica at (-x0,-y0))

General properties of Diophantine Equations can be found at:
https://en.wikipedia.org/wiki/Diophantine_equation

Techniques for solving linear Diophantine Equations can be found at:
https://www.math.cmu.edu/~bkell/21110-2010s/extended-euclidean.html and
https://brilliant.org/wiki/linear-diophantine-equations-one-equation

The extended Euclidean algorithm is a key sub-algorithm for solving
linear Diophantine equations.  The implementation here is based on the
version at https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm.

One bit of trivia.  This purely integer code.  In some situations avoiding
floating point has speed and portability benefits.
"""

from fractions import gcd
#rom math import gcd
#mport sys

#  do_self_check is a global variable which controls whether the integrity
#  of intermediate results is checked at strategic locations of execution.
do_self_check = False


def extended_euclidean(a, b):
    """Extended Euclidean Algorithm as presented in
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    This function returns five integers:  gcd(a,b), s, t, ha, and hb.
    s and t are integers satisfying the relation gcd(a,b) = s * a + b * t.
    If gcd(a,b) evenly divides c in equations of the form  a * x + b * y = c,
    then s and t are a particular solution to this equation.  ha and hb are the
    coefficients to the homogeneous equation:  0 = ha * a + hb * b."""

    s = 0
    r = b

    old_s = 1
    old_r = a

    while not (r == 0):
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    if not (b == 0):
        t = (old_r - old_s * a) // b
    else:
        t = 0

    ha = s
    hb = -s * a // b

    ab_gcd = old_r
    s = old_s

    if 0 > ab_gcd:
        ab_gcd = -ab_gcd
        s = -s
        t = -t

    #  Verify gcd(a,b) = s*a + t*b
    if do_self_check and ab_gcd != (s * a + t * b):
        print('ERROR(extendedEuclidean):  gcd != s*a + t*b  (gcd=%d  s=%d  a=%d  t=%d  b=%d)' % (ab_gcd, s, a, t, b))
        # s y s.e x i t(1)

    #  Verify 0 == ha * a + hb * b
    if do_self_check and 0 != (ha * a + hb * b):
        print('ERROR(extendedEuclidean):  0 != ha*a + hb*b  (ha=%d  a=%d  hb=%d  b=%d)' % (ha, a, hb, b))
        # s y s.e x i t(1)

    return ab_gcd, s, t, ha, hb


def points_to_eqn_1(x0, y0, x1, y1):
    """points_to_eqn_1() returns the coefficients of the line passing through me
    and the current reflection of trainer, given the location of me and the
    trainer."""

    diff_x = x1 - x0
    diff_y = y1 - y0

    #  a and b coefficients
    a = diff_y
    b = -diff_x

    #  c coefficient
    c = diff_y * x0 - diff_x * y0

    return [a, b, c]


def points_to_eqns_2(x0, y0, x1, y1, dx, dy):
    """points_to_eqn_2() returns the coefficients of the number of periods
    between each of the 4 types of replicas of me which (may) lie on the line
    passing through me and the trainer.  Solutions may or may not exist for each
    type of replica of me."""

    diff_x = x1 - x0
    diff_y = y1 - y0

    #  a and b coefficients
    a = diff_y * dx
    b = -diff_x * dy

    #  c coefficient for each type of replica of me
    c_px_py = 0
    c_mx_py = diff_y * x0
    c_px_my = -diff_x * y0
    c_mx_my = diff_y * x0 - diff_x * y0

    c = [c_px_py, c_mx_py, c_px_my, c_mx_my]

    return [a, b, c]


def test_interval(pri0, pri1, delta_pri, pri0_rep0):
    """test_interval() determines it current type of replica of me has a copy
    that lies in the interval between me and the trainer.  Since this works
    whether X coordinates or Y coordinates are used, the coordinate in use is
    designated 'pri' ('primary') rather than 'x' or 'y'."""

    #  x_lo and x_hi are the low and high values of interval between me and
    #  trainer
    pri_lo, pri_hi = [pri0, pri1] if pri0 < pri1 else [pri1, pri0]

    #  del_pri is the absolute value of spacing in prime coordinate of replicas
    del_pri = abs(delta_pri)

    #  Set k so that (pri0_rep0 + k * del_pri) is the max value that is less than
    #  or equal to pri_lo
    k = round((pri_lo - pri0_rep0) / del_pri)

    while pri_lo <= (pri0_rep0 + (k - 1) * del_pri):  # Zero or one iteration expected
        k -= 1

    while pri_lo > (pri0_rep0 + (k + 1) * del_pri):   # Zero or one iteration expected
        k += 1

    #  Given the above starting point, test locations spaced del_pri apart until either
    #  a) the location is in the interval between me and the trainer or
    #  b) goes past the other end of the interval
    pri_cur = pri0_rep0 + k * del_pri
    while pri_cur <= pri_hi:
        if pri_lo < pri_cur and pri_cur < pri_hi:
            if pri0 != pri_cur:
                return False

        #  Increment to next current type replica of me
        k += 1
        pri_cur = pri0_rep0 + k * del_pri

    return True


def verify_point(x, y, a, b, c):
    """Function verify_point() checks whether the point (x,y) lie on the line
    a*x + b*y = c.  This function is used for debugging."""

    #  Skip checking unless enabled
    if not do_self_check:
        return True

    if c != (a * x + b * y):
        print('NOT SOLUTION:  a=%d  x=%d  b=%d  y=%d  c=%d' % (a, x, b, y, c))
        # s y s.e x i t(1)
        return False

    return True


def solution(dimensions, my_position, trainer_position, max_distance):
    """solution() computes answers to the Bringing A Gun to a Trainer Fight
    challenge."""

    #  Unpack input variables into local variables
    dx, dy = dimensions
    mx, my = my_position
    tx, ty = trainer_position

    #  X and Y positions of me in even and odd replicas of room
    mx_eo = [mx, -mx, mx, -mx]
    my_eo = [my, my, -my, -my]

    #  X and Y positions of trainer in even and odd replicas of room
    tx_eo = [tx, dx - tx]
    ty_eo = [ty, dy - ty]

    #  Determine number of replicas in x and y
    num_rep_x = 1 + max_distance // dx
    num_rep_y = 1 + max_distance // dy

    #  My position is the starting position of all shot lines (x0,y0)
    x0, y0 = mx, my

    #  Initialize variables holding info about viable directions
    viable_dirs = {}

    #  Avoid square roots (and floating point) by working with squares of distances
    max_distance_squared = max_distance * max_distance

    #  Loop over replicas of room in x
    for rep_x in range(-num_rep_x, num_rep_x + 1):

        #  Loop over replicas of room in y
        for rep_y in range(-num_rep_y, num_rep_y + 1):

            #  Determine trainer position (x1,y1) in this replica
            x1 = rep_x * dx + tx_eo[rep_x % 2]
            y1 = rep_y * dy + ty_eo[rep_y % 2]

            #  Determine distance (squared) to trainer
            distance_squared = (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0)

            #  Process replica if trainer is within the range of the beam
            if distance_squared <= max_distance_squared:

                #  Get coefficients of line through me and this reflection of trainer
                [a0, b0, c0] = points_to_eqn_1(x0, y0, x1, y1)

                #  If requested, verify both target's reflection and my positions
                #   satisfy equation
                if do_self_check:
                    verify_point(x0, y0, a0, b0, c0)
                    verify_point(x1, y1, a0, b0, c0)

                #  Get coefficients of equations to solve for reflections of myself
                [a1, b1, c1_list] = points_to_eqns_2(x0, y0, x1, y1, dx, dy)

                #  Run the Extended Euclidean Algorithm on coefficients a and b
                ab_gcd, s, t, ha, hb = extended_euclidean(a1, b1)

                #  Process Diophantine equation for each of my reflection types
                is_viable = True
                for idx_c1 in range(len(c1_list)):

                    #  Get the c1 coefficient for equations for the current type
                    #  of replica of me
                    c1 = c1_list[idx_c1]

                    #  Get the remainder of c0 divided by gcd(a0,b0)
                    rem = c1 % ab_gcd

                    #  If zero is the remainder, the line through me and the
                    #  trainer also passes through current type of replica of
                    #  me.
                    if 0 == rem:

                        #  m (n) is the number of multiples of 2*dx (2*dy)
                        #  between solutions for the current type of replica of
                        #  me on the line through me and the current replica of
                        #  trainer.
                        if c1 == 0:
                            m = 0
                            n = 0
                        else:
                            q = c1 // ab_gcd

                            m = q * s
                            n = q * t

                        #  If requested, verify m and n are solutions to equation.
                        if do_self_check:
                            verify_point(m, n, a1, b1, c1)

                        #  delta_x (delta_y) is the spacing in x (y) between
                        #  current type of replica of me on line through me and
                        #  trainer.
                        delta_x = 2 * ha * dx
                        delta_y = 2 * hb * dy

                        #  (x0_rep0,y0_rep0) is the location of the 'anchor'
                        #  solution of current type of replica of me on line
                        #  through me and trainer.
                        x0_rep0 = 2 * m * dx + mx_eo[idx_c1]
                        y0_rep0 = 2 * n * dy + my_eo[idx_c1]

                        #  If requested, verify that (x0_rep0,y00) is a solution to
                        #  equation through me and reflection of trainer.
                        if do_self_check:
                            verify_point(x0_rep0, y0_rep0, a0, b0, c0)

                        if abs(x1 - x0) > abs(y1 - y0):
                            if not test_interval(x0, x1, delta_x, x0_rep0):
                                is_viable = False
                                break
                        else:
                            if not test_interval(y0, y1, delta_y, y0_rep0):
                                is_viable = False
                                break

                #  A shot to the current replica won't hit me first.  Only thing
                #  left is to avoid double counting the same direction
                if is_viable:

                    #  Create a string representing this direction
                    diff_x = x1 - x0
                    diff_y = y1 - y0
                    g = abs(gcd(diff_x, diff_y))

                    dir_str = '%d:%d' % (diff_x // g, diff_y // g)

                    #  Add a new entry in list of directions if this is new
                    if dir_str not in viable_dirs:
                        viable_dirs[dir_str] = 0

                    #  Increment count for this direction (count is not used)
                    viable_dirs[dir_str] += 1

    #  The answer is the number of entries in the dictionary of viable directions
    return len(viable_dirs)


if __name__ == '__main__':
#   print(solution([3, 2], [1, 1], [2, 1], 4))
#   print(solution([3, 2], [1, 1], [2, 1], 5))
#   print(solution([300, 275], [150, 150], [185, 100], 500))
#   print(solution([60, 55], [30, 30], [37, 20], 100))
    print(solution([42, 59], [34, 44], [6, 34], 5000))
