from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()

    def enqueue(self,item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue è vuoto")
        return self.__data.popleft()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("queue vuota")
        return self.__data[0]
    
    def isEmpty(self):
        return len(self.__data) == 0
    
    def size(self):
        return len(self.__data)
    
    def __repr__(self):
        return f"{list(self.__data)}"
    
q = Queue()
lista = ["Mario","Giulia","Tonino","Rosa"]
for i in lista:
    q.enqueue(i)

print(f"Questa è la fila dal macellaio {q}")
next = q.dequeue()
print(f"Servo: {next}")

q.enqueue("Enzo")
print(f"Arriva un nuovo cliente: Enzo")
print(f"Ci sono ancora {q.size()} persone in fila!")
print(f"In fila ci sono ancora queste persone: {q}")

#Servo a tutti
for i in lista:
    next = q.dequeue()
    print(f"Servo: {next}")


if q.isEmpty() == True:
    print(F"Non c'è più nessuno in fila {q}")