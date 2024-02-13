class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, n=0, max=0):
        self.n = n
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration