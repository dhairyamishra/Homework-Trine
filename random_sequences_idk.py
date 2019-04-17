import random
numbers = []
for i in range(10):
    j = int(random.uniform(0, 100))
    numbers.append(j)
print(numbers)
print(*numbers[1::1])
for i in range(10):
    if numbers[i] % 2==0:
        print(numbers[i]," ", end="")
print()
print(*numbers[::-1])
print(numbers[0], numbers[-1])
print("\n"*5)
