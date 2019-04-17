f= open("gym.txt", "r")
conts= int(f.readline())
nloop=[]
for i in range(conts):
    nloop.append([])
print(nloop)
ppl=[]
print(conts)
line = f.readline().strip("\n")
for i in range(conts*2):
    if line=="":
        line=f.readline().strip("\n")
    else:
        ppl.append(line)
        line= f.readline().strip("\n")
print(ppl)
for i in range(0,conts):
    x= ppl[i].split()
    nloop[i]=x
print(nloop)
total = 0
nloop2 = nloop[0][1:]
print(nloop2)
big=0
small=10

print("Contestants\t\t\t\t\t\t Scores")
for i in range(conts):
    print(nloop[i][0],"\t\t\t\t\t\t", *nloop[i][1:])
for i in range(conts):
    nloop2 = nloop[i][1:]
    for q in range(len(nloop2)):
        nloop2[q]= float(nloop2[q])

    nloop2.sort()
    total= sum(nloop2[1:-1])/6
    print("Total Score of {} is: {}".format(nloop[i][0],format(total,".2f")))
    if total>float(big):
        big=total
    if total<float(small):
        small=total

print("The highest total score amongst the contestants is: ", format(big,".2f"))
print("The lowest total score amongst the contestants is: ",format(small,".2f"))





f.close()
