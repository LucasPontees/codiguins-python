from collections import deque

fila = deque()

fila.append("A") 
fila.append("B")
fila.append("C")

print(fila)      

primeiro = fila.popleft()
print("Saiu:", primeiro)
print(fila)       
