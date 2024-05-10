#Pseudo: create in this module calculations.py two functions to calculate the area of a square and the circumference of a cirlce
# area of a square is length * width (l * w)
# circumference of a circle is 2*pi*radius
# need to import math.pi for the function
# step 1
# import math
# def area_of_square_footage(length,width):
#     """Calculate the square footage of a house"""
#     area = length * width 
#     return f' the area of the square house is {area}'
    
#     # Step 2
# def circumference_of_a_circle(radius):
#     """calculate the circumference of a circle"""
#     from math import pi as p  #getting the pi value from math by using import from
#     circumference = 2 * p * radius  #the math formula for calculating the circumference of a circle is 2 x pi x radius
#     return f'the circumference of the circle is {circumference}'


def area_of_square_footage(length,width):
    """Calculate the square footage of a house"""
    # check if length and width are positive numbers
    if length > 0 and width > 0:
        area = length * width  #storing the formula in a variable
        return f'{area} square units'
    else:
        return 'Length and width must be positive numbers.'
    # Step 2
def circumference_of_a_circle(radius):
    """calculate the circumference of a circle"""
    from math import pi as p  #getting the pi value from math by using import from
    # check if the radius is a positive number
    if radius > 0:
        circumference = 2 * p * radius  #the math formula for calculating the circumference of a circle is 2 x pi x radius
        return f'{circumference} units'
    else:
        return 'radius must be a positivr number'