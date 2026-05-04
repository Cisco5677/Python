from collections import deque

queue = deque(["luca", "sara", "mario"])

queue.append("anna")
primo = queue.popleft()
print(primo)  
