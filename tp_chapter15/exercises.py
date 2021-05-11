from math import sqrt

class Point:
    """Instances point objects"""

class Rectangle:
    """Represents a rectangle
    
    attributes: height, width, corner"""

# Instance 2 points
point1 = Point()
point2 = Point()

# Assign coordinates to first point
point1.x = 2
point1.y = 3

# Assign coordinates to second point
point2.x = 7
point2.y = 9

## Compute the distance between 2 points
# @param p1, p2 2 points
# @return the distance
def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    d = sqrt(dx**2 + dy**2)
    return d

# Call distance() and display the result
# print(distance(point1, point2))

# Instance a rectangle
rect = Rectangle()

# Assign attributes
rect.height = 50
rect.width = 100
rect.corner = Point() # attribute corner is an embedded object
rect.corner.x = 3
rect.corner.y = 4
