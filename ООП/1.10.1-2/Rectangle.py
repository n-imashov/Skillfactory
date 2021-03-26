# 1.10.1
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f'x: {self.x} \ny: {self.y} \nw: {self.width} \nh: {self.height}'


figure = Rectangle(5, 10, 50, 100)
print(figure)


# 1.10.2
class Rectangle2D:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return f"Прямоугольник (длина, высота, площадь): {self.width}, {self.height}, {self.width * self.height}"


figure = Rectangle2D = Rectangle2D(5, 10)
print(Rectangle2D.get_area())
