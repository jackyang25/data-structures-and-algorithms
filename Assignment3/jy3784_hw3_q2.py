
import ctypes  # provides low-level arrays

def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def insert(self, index, val):

        if not (-self.n <= index <= self.n - 1):
            raise IndexError('invalid index')

        elif self.n < self.capacity:

            for i in range(self.n, index, -1):
                self.data[i] = self.data[i - 1]

            self.data[index] = val

            self.n = self.n + 1

        elif self.n >= self.capacity:
            self.resize(self.capacity * 2)

            for i in range(self.n, index, -1):
                self.data[i] = self.data[i - 1]

            self.data[index] = val

            self.n = self.n + 1



    def pop(self, index = None):

        temp = ""

        if (self.n == 0):
            raise IndexError('invalid index')


        elif index is not None:
            if -self.n < -index < self.n:

                temp = self.data[index]

                self.data[index] = None

                for i in range(index+1, self.n):

                    self.data[i-1] = self.data[i]

                self.data[self.n - 1] = None

                self.n = self.n - 1

            else:
                raise IndexError('invalid index')


        elif (self.n > 0):
            temp = self.data[self.n - 1]

            self.data[self.n - 1] = None

            self.n = self.n - 1

        if self.n < (self.capacity * 1 // 4):
            self.resize(self.capacity // 2)

        return temp



    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'


    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times
