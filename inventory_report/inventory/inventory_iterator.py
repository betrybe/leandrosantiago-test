from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, sequence):
        self.index = 0
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.sequence[self.index - 1]
        except IndexError:
            raise StopIteration
