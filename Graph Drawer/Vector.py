class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(" + str(round(self.x, 2)) + ", " + str(round(self.y, 2)) + ")"

    def addV(self, v):
        newX = self.x + v.x
        newY = self.y + v.y
        return Vector(newX, newY)

    def vectorTo(self, v):
        dx = v.x - self.x
        dy = v.y - self.y
        return Vector(dx, dy)

    def length(self):
        d2 = (self.x)*(self.x) + (self.y)*(self.y)
        return d2 ** 0.5

    def unitVector(self):
        l = self.length()
        return Vector(self.x / l, self.y / l)

    def scalarMultiply(self, p):
        return Vector(self.x * p, self.y * p)
        