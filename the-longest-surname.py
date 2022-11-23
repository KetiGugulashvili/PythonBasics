x = []
for i in range(5):
    name = input('Please enter surname of your friend (' + str(i + 1) + ' from 5): ')
    x.append(name)

high = x[0]
for i in x:
    if len(i) > len(high):
        high = i

print(high + ' has the longest surname from your friends: ' + str(len(high)) + ' letters')