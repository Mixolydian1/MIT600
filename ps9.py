# 6.00 Problem Set 9
#
# Name: Adam Capulong

from string import *

INPUT_FILENAME = "shapes.txt"

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#

class Triangle(Shape):
    def __init__(self, b, h):
        """
        h: height length of triangle
        b: base length of triange
        """
        self.h = float(h)
        self.b = float(b)
    def area(self):
        """
        Returns area of triangle.
        """
        return 0.5 * self.h * self.b
    def __str__(self):
        return "Triangle with height " + str(self.h) + " and base " + str(self.b)
    def __eq__(self, other):
        return type(other) == Triangle and self.h == other.h and self.b == other.b

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(object):
    def __init__(self):
        """
        Initialize any needed variables
        """

        self.shapeList = []

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        foundMatch = False
        for shape in self.shapeList:
            if shape.__eq__(sh):
                foundMatch = True
        if foundMatch == False:
            self.shapeList.append(sh)

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        return iter(self.shapeList)

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        response = ""
        for shape in self.shapeList:
            if type(shape) == Circle:
                response = response + shape.__str__() + "\n"
        for shape in self.shapeList:
            if type(shape) == Square:
                response = response + shape.__str__() + "\n"
        for shape in self.shapeList:
            if type(shape) == Triangle:
                response = response + shape.__str__() + "\n"
        return response         
                
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largestShapes = []
    currentLargestAreaValue = 0
    for shape in shapes:
        #print "TESTING " + shape.__str__()
        if shape.area() > currentLargestAreaValue:
            #print "found shape of bigger area w/ a value of " + str(shape.area) + " from shape " + shape.__str__()
            largestShapes = []
            currentLargestAreaValue = shape.area()
            largestShapes.append(shape.__str__())
        elif shape.area() == currentLargestAreaValue:
            #print "found shape of equal area w/ a value of " + str(shape.area) + " from shape " + shape.__str__()
            largestShapes.append(shape.__str__())
        else:
            continue
    
    return tuple(largestShapes)


    ## TO DO

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    inputFile = open(filename)
    inputFileList = []
    for line in inputFile:
        inputFileList.append(line.split(","))

    shapeSet = ShapeSet()
    for line in inputFileList:
        if line[0] == "circle":
            shapeSet.addShape(Circle(line[1]))
        elif line[0] == "square":
            shapeSet.addShape(Square(line[1]))
        elif line[0] == "triangle":
            shapeSet.addShape(Triangle(line[1],line[2]))
        else:
            print "[-] Attempted to add an undefined shape"

    return shapeSet



triangle1 = Triangle(1.1,2.2)
#print triangle1.__str__()
triangle2 = Triangle(1.1,2.2)
#print triangle1.__eq__(triangle2)
#print type(triangle1) == Triangle

shapeSet = readShapesFromFile(INPUT_FILENAME)


#print shapeSet.__str__()
"""
for shape in shapeSet:
    print shape.__str__()
    print shape.area()
"""
print type(findLargest(shapeSet))