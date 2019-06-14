class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        pass

    def get(self):
        # return storage list for every element that is not None
        return [i for i in self.storage if i]
