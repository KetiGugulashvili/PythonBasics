f = open("ints.txt", "r")
intsList = f.readlines()
newList = []

for i in intsList[0:len(intsList)-1]:
    x = i[0:len(i)-1]
    newList.append(int(x))

newList.append(int(intsList[len(intsList)-1]))

f = open("ints.txt", "w")
f.write(str(max(newList)))
