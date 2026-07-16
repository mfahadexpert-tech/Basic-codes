class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_point_on_line(self, point):

        return self.a * point.x + self.b * point.y + self.c ==0


line = Line(1, 1, -2)
pt = Point(1, 1)

print(line.is_point_on_line(pt))