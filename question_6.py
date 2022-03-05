''' Brady Neeb
    Scientific Computing Midterm Exam Question #6
    <bneeb@mail.smcvt.edu>

    Write a program to compute the mathematical constant 'e', the base of the natural logarithms, 
    from the definition: e = lim(n->inf) (1 + 1/n)^n. Specifically, compute (1 + 1/n)^n for n = 10^k,
    k = 1, 2, ... , 20. Determine error in your successive approximations by comparing them with the 
    value of exp(1). Does the error always decrease as n increases? Explain your results.

    Results:

        e at k = 8 has the closest margin of error to actual e. 

        Output:
            - Iteration 8:
            --- Calculated e: 2.7182817863957975
            --- Actual e:     2.718281828459045
            --- Error:        4.206324755173796e-08
        
        Error in this example, does not always decrease as n increases. There is a middlepoint at k=8 where 
        we get the maximum error margin, then the results get much worse and further from exp(1) as k increases.
'''

import math


def solve():
    ''' Solve for e '''

    exp = math.exp(1)
    min_error = 1   # Expect to find an error less than 1

    for k in range(1, 21):

        # Calculate e
        n = 10 ** k
        e = (1 + (1/n))**n

        # Find error
        error = abs(e - exp)

        # Print information
        print("-----------------")
        print(f"- Iteration {k}:")
        print(f"--- Calculated e: {e}")
        print(f"--- Actual e:     {exp}")
        print(f"--- Error:        {error}")
        print("-----------------")

        # Check which iteration has smallest error margin
        if error < min_error:
            min_error = error
            min_error_iteration = k

    # Print min error info
    print(f"Minimum error margin: {min_error} at index {min_error_iteration}")


if __name__ == '__main__':

    solve()
