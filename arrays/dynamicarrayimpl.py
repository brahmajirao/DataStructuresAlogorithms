import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')

        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self._increase_capacity(self.capacity*2)

        self.A[self.n] = element
        self.n += 1

    def _increase_capacity(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap*ctypes.py_object)()


if __name__ == "__main__":
    myArray = DynamicArray()
    print(myArray.__len__())
    myArray.append(5)
    print(myArray.__len__())
    myArray.append(55)
    print(myArray.__getitem__(1))