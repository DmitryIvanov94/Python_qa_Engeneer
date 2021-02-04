import math


class Figure:
    def __init__(self, name, angles, a=3, b=4, c=5, r=10):
        self.name = name
        self.angles = angles

        if name == 'square':
            self.a = a
        elif self.name == 'rectangle':
            self.a = a
            self.b = b
        elif self.name == 'triangle':
            self.a = a
            self.b = b
            self.c = c
        elif self.name == 'circle':
            self.r = r

    @property
    def area(self):
        if self.name == 'square' and self.angles == 4 and self.a > 0:
            return self.a ** 2
        elif self.name == 'rectangle' and self.angles == 4 and self.a > 0 and self.b > 0:
            return self.a * self.b
        elif self.name == 'triangle' and self.angles == 3 and self.a > 0 and self.b > 0 and self.c > 0 \
                and self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        elif self.name == 'circle' and self.angles == 0 and self.r > 0:
            return math.pi * (self.r ** 2)
        else:
            return ValueError("Wrong parameters of figure")

    @property
    def perimeter(self):
        if self.name == 'square' and self.angles == 4 and self.a > 0:
            return self.a * 4
        elif self.name == 'rectangle' and self.angles == 4 and self.a > 0 and self.b > 0:
            return (self.a + self.b) * 2
        elif self.name == 'triangle' and self.angles == 3 and self.a > 0 and self.b > 0 and self.c > 0 \
                and self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            return self.a + self.b + self.c
        elif self.name == 'circle' and self.angles == 0 and self.r > 0:
            return 2 * math.pi * self.r
        else:
            return ValueError("Wrong parameters of figure")

    def add_area(self, obj):
        if not isinstance(obj, Figure):
            return TypeError("Argument must be instance of Figure class")
        else:
            return obj.area + self.area
