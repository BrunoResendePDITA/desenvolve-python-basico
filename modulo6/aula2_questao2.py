import random

num_elementos = random.randint(5, 20)
elementos = []

for num in range(num_elementos):
    elementos.append(random.randint(1, 10))

print(elementos)
print(sum(elementos))
print(sum(elementos)/len(elementos))
