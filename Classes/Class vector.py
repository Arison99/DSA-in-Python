class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x **2 + self.y **2) ** 0.5
    
u = Vector(3, 4)

print(u.norm)
print(Vector(5, 12).norm())