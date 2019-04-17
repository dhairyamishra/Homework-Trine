f  = open("data1.txt", "r")
line = f.readline()
numbers= line.split(" ")
print(numbers)
c=[]
summ = 0
for i in range(0, len(numbers)):
    if i%2==0:
        summ = summ + int(numbers[i])

    else:
        summ = summ - int(numbers[i])
i = 0
while numbers[i] != numbers[-1]:
    if i%2==0:
        c.append(numbers[i])
        c.append("-")
    else:
        c.append(numbers[i])
        c.append("+")
    i += 1
c.append(numbers[-1])



print("The sequence is :")
print(*c," = ", summ)



f.close()
