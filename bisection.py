''' 
Brady Neeb
Scientific Computing Midterm Exam Question #1
<bneeb@mail.smcvt.edu>
'''

import math

ERROR = 0.00000000000001   # Error is within 15 places of pi


def f(x):
    ''' Hard coded function f(x) = sin(x) '''
    return math.sin(x)


def bisection(a, b):
    ''' This function will calculate the roots of a function on interval [a,b] '''

    # Save original [a,b] values for print statements later on
    a_ = a
    b_ = b

    # Check if there is a root to be found
    if f(a) * f(b) > 0:
        print("No root can be found!")

    # Find the root
    else:

        # Loop through while in margin of error
        while (b-a)/2 > ERROR:

            # Calculate a midpoint
            c = (b + a) / 2

            # Condition for 0 root
            if f(c) == 0:
                print(f"Root found on interval [{a_},{b_}]! {c}")
                return

            # Go to the side that root is closest to
            elif f(a)*f(c) < 0:
                b = c
            else:
                a = c

        print(f"Root found on interval [{a_},{b_}]! {c}")


if __name__ == '__main__':

    bisection(-1, 1)
    bisection(2, 5)
