class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def __increase_curent__(self):
        # increase current count
        self.current += 1
        # if resulting current count is bigger than last index in storage list (capacity - 1 )
        # start at first index (capacity = 0)
        if self.current > self.capacity - 1:
            self.current = 0

    def append(self, item):
        # insert item to specific index (current)
        self.storage[self.current] = item
        # increase current value for next append method call
        self.__increase_curent__()

    def get(self):
        # return storage list for every element that is not None
        return [i for i in self.storage if i]


a = RingBuffer(5)

a.append('a')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')
a.append('b')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')
a.append('c')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')
a.append('d')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')
a.append('e')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')

a.append('f')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')
a.append('g')
print(f'current: {a.current}, storage: {a.storage}, capacity: {a.capacity}')
