class CircularQueue:
    def __init__(self, capacity):
       self.capacity=capacity+1
       self.data=[None]*self.capacity
       self.front=0
       self.rear=0
       def is_empty(self):
           return self.front==self.rare
def is_full(self):
    return self.rear+1%self.capacity==self.front
