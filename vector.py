from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

     '''__repr__ Allows for our return values to be represented LIKE a 
     string instead of object locations. __str__ was not used, because
     since we are using mathematical operations, the numbers must be
     integers or floats and not actual strings, such as Vector('1', '4')
     '''
    def __repr__(self): 
        ''' Below is the original return statement listed in Fluent Python. 
        From Google I learned that the %r signs were string formats using variable replacement.
        Once I learned that, I decided to replace it with the F-string format,
        which I already knew and prefer.
        ''' 
        # # return 'Vector(%r, %r)' % (self.x, self.y)
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # This method was not listed in Fluent Python - I added it myself.
    def __truediv__(self, scalar): 
        return Vector(self.x / scalar, self.y / scalar) 

    # This method was not listed in Fluent Python - I added it myself.
    def __pow__(self, scalar): 
        return Vector(self.x ** scalar, self.y ** scalar) 

        # This method was not listed in Fluent Python - I added it myself.

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)


v1 = Vector (2, 1)
v2 = Vector (3, 3)

print(v1 + v2)
print(v1 * 2)
print(v2 * 2)
print(v2 / 3)
print(v1 ** 3)
print(v2 ** 2)
print(v2 - v1)