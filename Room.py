class Room:
    def __init__(self, number, capacity):
        self._number = number
        self._capacity = capacity

    def get_number(self): return self._number
    def get_capacity(self): return self._capacity
