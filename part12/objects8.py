class PointsList(object):
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def __len__(self):
        return len(self.points)

    def __contains__(self, p):
        return p in self.points

    def __add__(self, p):
        # The + operator can be used to combine 2 lists.
        return self.points + p.points 

    def __str__(self):
        return str(self.points)


p = PointsList()
p.add_point(2, 4)
p.add_point(-1, -5)
p.add_point(5, 11)
print(p)

# Demonstrate the __len__ method
print(len(p))

# Demonstrate the __contains__ method
if (2, 4) in p:
    print('We have 2,4!')
else:
    print('2, 4 was not found.')

# Demonstrate the __add__ method
other = PointsList()
other.add_point(7, 9)
other.add_point(-4, -11)
print(p + other)

