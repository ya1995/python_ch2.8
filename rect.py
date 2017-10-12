class Rect:
    count_of_instance = 0

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        Rect.count_of_instance += 1

    def __del__(self):
        Rect.count_of_instance -= 1

    def __str__(self):
        return "Rect({0}, {1}, {2}, {3})".format(self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        return "Rect({0}, {1}, {2}, {3})".format(self.x1, self.y1, self.x2, self.y2)

    def area(self):
        return (self.x2-self.x1) * (self.y2-self.y1)

    def draw(self):
        print("Rect({0}, {1}, {2}, {3})를 그렸습니다.".format(self.x1, self.y1, self.x2, self.y2))

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()