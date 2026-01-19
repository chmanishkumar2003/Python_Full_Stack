class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,ele):
        self.queue.append(ele)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        return False
    
    def size(self):
        return len(self.queue)

myQueue= Queue()
myQueue.enqueue('A') 
myQueue.enqueue('B')
myQueue.enqueue('C')
myQueue.enqueue('D')

print("Queue",myQueue.queue)
print("Pop queue at element",myQueue.dequeue())
print("Queue after pop",myQueue.queue)
print("Size of queue",myQueue.size())
print("Is Queue empty,",myQueue.isEmpty())
print("Peek of queue",myQueue.peek())
