f = open("./elements","r")
intsList = f.readlines()
newSet = set()

for i in intsList[0:len(intsList)-1]:
    x = i[0:len(i)-1]
    newSet.add(x)

newSet.add(intsList[len(intsList)-1])
print(newSet)
