class Queue:
    
    def __init__(self,):
        self.queue = []
        
    def deqeue(self):
        if len(self.queue) > 0:
            primero = self.queue[-1]
            del self.queue[-1]
            return primero
        
    def enqueue(self, valor):
        self.queue.insert(0,valor)
        
    
cola = Queue()
print(cola.enqueue(3))
print(cola.enqueue(1))
print(cola.enqueue(2))


print(cola.deqeue())
print(cola.deqeue())
print(cola.deqeue())