class Stack:
    def __init__(self):
        self.__data= []

    def push(self,item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop nello stack è vuoto")
        return self.__data.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Lo stack è vuoto")
        return self.__data[-1]
    
    def isEmpty(self):
        return len(self.__data) == 0
    
    def size(self):
        return len(self.__data)
    
    def __repr__(self):
        return f"Stack({self.__data})"



history = Stack()
forward = Stack()

history.push("Google.com")
history.push("wikipedia.com")
history.push("Python.org")

current = history.pop()
print(f"---- Web Services Stack ---- \n")
print(f"Pagina corrente: {current}")
print(f"Cronologia: {history} \n")

forward.push(current)
current = history.pop()

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward} \n")

history.push(current)
current = forward.pop()

print(f"Pagina corrente: {current}")  
