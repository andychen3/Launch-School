# https://launchschool.com/exercises/699c68e4

class CircularBuffer:

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = [None] * buffer_size
        self.front = 0
        self.oldest = 0
        self.end = len(self.buffer) - 1

    def put(self, value):
        """
        We check if buffer is full
        if buffer is full we remove the oldest
        If not full we add where front is pointing
        """
        if self.buffer[self.front] == None:
            self.buffer[self.front] = value
            self.front += 1
        elif self.buffer[self.front] != None:
            self.buffer[self.oldest] = value
            self.front = self.oldest
            self.oldest += 1
        
        if self.front > self.end:
            self.front = 0

        if self.oldest > self.end:
            self.oldest = 0
        
    def get(self):
        """
        Remove and return the oldest object in the buffer
        Return None if the buffer is empty
        Update oldest
        """
        if self.buffer[self.oldest] == None:
            return None
        
        if self.buffer[self.oldest] != None:
            oldest = self.buffer[self.oldest]
            self.buffer[self.oldest] = None
            self.oldest += 1
        
        if self.oldest > self.end:
            self.oldest = 0
        
        return oldest

"""
self.front = 0
self.oldest = 0
self.end = 2
[4, 5, 6]




"""

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True