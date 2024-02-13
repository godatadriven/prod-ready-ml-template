class ToPower:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, n=0, max=0, power=2):
        self.n = n
        self.max = max
        self.power=power

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.power ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration