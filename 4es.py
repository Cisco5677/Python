history = ["google.com","wikipedia.org","python.org"]
forward= []

current = history.pop()
print(f"Pagina corrente: {current}")
print(f"Cornologia: {history}")

forward.append(current)
current = history.pop()

history.insert(1, "yahoo.com")

print(f"Pagina corrente: {current}")
print(f"Cornologia: {history}")
print(f"Avanti: {forward}")
print(f"Hisotry[1]: {history[1]}")
forward.append(current)
current = history.pop()

print(f"Hisotry[0]: {history[0]}")

history.pop(0)
#history.remove("google.com")


'''
print(f"Pagina corrente: {current}")
print(f"Cornologia: {history}")
print(f"Avanti: {forward}")


history.append(current)
current = forward.pop()

print(f"Pagina corrente: {current}")        # wikipedia.org
print(f"Cronologia: {history}")             # ['google.com']
print(f"Avanti: {forward}")                 # ['python.org']
'''