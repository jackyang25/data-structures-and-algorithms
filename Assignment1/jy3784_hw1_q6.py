class Vector:

    def __init__(self, d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __len__(self):

        return len(self.coords)

    def __getitem__(self, j):

        return self.coords[j]

    def __setitem__(self, j, val):

        self.coords[j] = val

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __add__(self, other):
        if (len(self) != len(other)):

            raise ValueError("dimensions must agree")
        result = Vector(len(self))

        for j in range(len(self)):

            result[j] = self[j] + other[j]
        return result

    def __neg__(self):
        lst = []
        for item in self.coords:
            if item > 0:
                lst.append(item * -1)
        return Vector(lst)

    def __mul__(self, other):
        if isinstance(other, int):
            lst = []
            for i in range(len(self.coords)):
                lst.append(self.coords[i] * other)
            return Vector(lst)

        else:
            lst = []
            for i in range(len(other.coords)):
                lst.append(other[i] * self[i])
            return sum(lst)

    def __rmul__(self, other):
        lst = []

        for item in self.coords:
            lst.append(3 * item)
        return Vector(lst)

    def __eq__(self, other):

        return self.coords == other.coords

    def __ne__(self, other):

        return not (self == other)

    def __repr__(self):

        return str(self)




