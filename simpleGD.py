"""
This is my first try at doing gradient descent. This program assumes basic
knowledge of calculus.

Functions:

z = x^2 + y^2 - 2x - 6y + 14      # 3d elliptic paraboloid

dz/dx = 2x - 2  : partial derivative of z with respect to x
dz/dx = 2y - 6  : partial derivative of z with respect to y

Gradient Descent will be used to arrive at the min of the above function, z.

"""

from numpy import *         # I import with * only beacuse numpy is the only library I use.
                            # This lets you call function from numpy with out writing numpy.someFunction()
                            # However this is not good if you have more than one library, it gets confusing.

def gradientDescentStep(currentX, currentY, learningRate):
    gradientX = 2 * currentX - 2                       # derivatives as from above.
    gradientY = 2 * currentY - 6
    newX = currentX - (gradientX * learningRate)       # This part is explained in detail
    newY = currentY - (gradientY * learningRate)       # in the readme.
    return [newX, newY]

def gradientDescent(startX, startY, numIterations, learningRate):
    X = startX
    Y = startY
    for i in range(numIterations):                     # The x and y values are continualy fed into the loop.
        X, Y = gradientDescentStep(X, Y, learningRate) #    starting at zero
    return [X, Y]

def main():
    learningRate = 0.001                               # learningRate affects how fast the conversion happens.
    iterations = 10000                                 # Higher number of iterations will increase accuracy.
    startX = 0
    startY = 0
    [x, y] = gradientDescent(startX, startY, iterations, learningRate)
    z = x**2 + y**2 - 2*x - 6*y + 14
    print("unrounded values: ")
    print("x = {0}, y = {1}, z = {2}".format(x, y, z))             # Printing the x, y and z values.
    x = round(x)
    y = round(y)
    z = round(z)
    print("rounded values: ")
    print("x = {0}, y = {1}, z = {2}".format(x, y, z))             # Printing the rounded x, y and z values.

if __name__ == "__main__":
    main()
