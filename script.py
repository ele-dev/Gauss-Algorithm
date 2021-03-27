#!/usr/bin/env python3

# method that reads in equation with form: ax + by + cz = d
def readEquation():
    print("Equation form ax + bx + cz = d")
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))
    return [a, b, c, d]

# method that simply prints out the current matrix 
def printMatrix(matrix):
    for i in matrix:
        print(i)

# do the a coefficient elimination
def aElimination():
    factor1 = -matrix[0][0]
    factor2 = matrix[1][0]
    factor3 = matrix[2][0]
    
    # overwrite equation 2 with the result of the addition of the scaled equ1 & equ2
    matrix[1][0] = factor2 * matrix[0][0] + factor1 * matrix[1][0]
    matrix[1][1] = factor2 * matrix[0][1] + factor1 * matrix[1][1]
    matrix[1][2] = factor2 * matrix[0][2] + factor1 * matrix[1][2]
    matrix[1][3] = factor2 * matrix[0][3] + factor1 * matrix[1][3]

    # overwrite equation 3 with the result of the addition of the scaled equ1 & equ3
    matrix[2][0] = factor3 * matrix[0][0] + factor1 * matrix[2][0]
    matrix[2][1] = factor3 * matrix[0][1] + factor1 * matrix[2][1]
    matrix[2][2] = factor3 * matrix[0][2] + factor1 * matrix[2][2]
    matrix[2][3] = factor3 * matrix[0][3] + factor1 * matrix[2][3]

# do the b coefficient elimination
def bElimination():
    factor2 = -matrix[1][1]
    factor3 = matrix[2][1]

    # Overwrite equation 3 with the result of the addition of the scaled equ2 & equ3
    matrix[2][0] = factor3 * matrix[1][0] + factor2 * matrix[2][0]
    matrix[2][1] = factor3 * matrix[1][1] + factor2 * matrix[2][1]
    matrix[2][2] = factor3 * matrix[1][2] + factor2 * matrix[2][2]
    matrix[2][3] = factor3 * matrix[1][3] + factor2 * matrix[2][3]


# Main part
print("Gauss Elimination with 3 unknown variables\n")

# Read in the 3 equations
print("Enter the coefficents for Equation I")
equ1 = readEquation()
print("Enter the coefficents for Equation II")
equ2 = readEquation()
print("Enter the coefficents for Equation III")
equ3 = readEquation()

# construct 3x4 Matrix 
matrix = [equ1, equ2, equ3]

# show the initial state of the matrix
print("Original Matrix:")
printMatrix(matrix)

# do the a elimination 
print("A elimination part:")
aElimination()
printMatrix(matrix)

# do the b elimination 
print("B elimination part:")
bElimination()
printMatrix(matrix)

# calculate the 3 variables x, y and z
try:
    z = matrix[2][3] / matrix[2][2]
    y = (matrix[1][3] - z * matrix[1][2]) / matrix[1][1]
    x = (matrix[0][3] - z * matrix[0][2] - y * matrix[0][1]) / matrix[0][0]
except:
    print("This Equation system has no clear solution")
    exit()


# Print final result
print("Result: ")
print("X = " + str(x))
print("Y = " + str(y))
print("Z = " + str(z))
print("\n")
