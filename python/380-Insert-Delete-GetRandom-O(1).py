from random import choice

class RandomizedSet:

    def __init__(self):
        self.hashSet: dict[int, int] = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hashSet:
            return False
        self.hashSet[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashSet:
            return False
        del self.hashSet[val]
        return True

    def getRandom(self) -> int:
        return choice(list(self.hashSet.keys()))
