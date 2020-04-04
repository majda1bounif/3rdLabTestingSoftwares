import math
import types


# def complex(radius,x, y):
# return isinstance(x, types.Tuple) and isinstance(x, types.Tuple)and isinstance(x, types.Tuple)
# return complex()

def check(radius, x, y):
    angle = math.atan2(x, y) * (180 / math.pi)
    if 0 <= x <= radius and 0 <= y <= radius and x ** 2 + y ** 2 <= radius ** 2 and angle == 45 \
            or (-1) * radius <= y <= 0 and (-1) * radius <= x <= 0 and x * x + y * y <= radius * radius and angle == 45:
        return True
    else:
        return False
    return check()
    # or -radius <= y <= 0 and -radius <= x <= 0 and x*x + y*y <= radius*radius and math.atan2(x, y) == -(math.pi /
