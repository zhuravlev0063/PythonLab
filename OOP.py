import math

class Shape:
    def __init__(self, identifier):
        self.identifier = identifier

class Triangle(Shape):
    def __init__(self, identifier, a, b, c):
        super().__init__(identifier)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Используем формулу Герона для площади треугольника
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def move(self, dx, dy):
        print(f"{self.identifier}: Перемещение треугольника на ({dx}, {dy})")

class Tetragon(Shape):
    def __init__(self, identifier, side1, side2, side3, side4):
        super().__init__(identifier)
        self.sides = [side1, side2, side3, side4]

    def area(self):
        return self.sides[0] * self.sides[1]

    def move(self, dx, dy):
        print(f"{self.identifier}: Перемещение четырехугольника на ({dx}, {dy})")

def compare(t1, t2):
    try:
        area_t1 = t1.area()
        area_t2 = t2.area()
        if area_t1 > area_t2:
            print(f"{t1.identifier} больше {t2.identifier}")
        elif area_t1 < area_t2:
            print(f"{t1.identifier} меньше {t2.identifier}")
        else:
            print(f"{t1.identifier} и {t2.identifier} равны по площади")
    except Exception as e:
        print("Ошибка при сравнении площадей:", e)


triangle = Triangle("Triangle1", 3, 4, 5)
tetragon = Tetragon("Tetragon1", 5, 6, 5, 6)

triangle.move(2, 3)
tetragon.move(-1, 4)
compare(triangle, tetragon)
