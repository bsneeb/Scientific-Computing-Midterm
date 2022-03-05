''' Brady Neeb
    Scientific Computing Midterm Exam Question #4
    <bneeb@mail.smcvt.edu>    

    Improve Gauss' Method code to read the matrix from a file. 
    Format:
        - One line per row
        - Floating point numbers seperated by spaces
        - No need for extensive error handling, but should be able to spot
        the number of cols in a for different than another
'''

import os


def gauss(A, num_rows, num_cols):
    ''' Gauss elimination in python. '''

    for k in range(0, num_rows-1):

        for i in range(k+1, num_rows):  # Row that will be changed

            pivot_mult = A[i][k]/A[k][k]

            for j in range(0, num_cols):  # Column number in that row

                A[i][j] = A[i][j] - pivot_mult*A[k][j]

    print("solution is: ", A)


def parse_file(filename):
    ''' Parses file to be used in Gauss elimination '''

    A = []

    with open(filename) as f:
        for i, line in enumerate(f):

            # Append the rows to A
            A.append([float(x) for x in line.split()])

            # Error check
            if len(A[0]) != len(A[i]):
                print(f"[ERROR] - Rows in file have different lengths.")
                return

    return A


if __name__ == '__main__':

    A = parse_file('matrix.txt')

    num_rows = len(A)
    num_cols = len(A[0])

    gauss(A, num_rows, num_cols)
