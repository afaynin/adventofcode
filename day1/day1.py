list1 = []
list2 = []
with open('input.txt', 'r') as file:
    content = file.read()
    content = content.splitlines()
    for cont in content:
        if cont.split()[0] is not None:
            list1.append(int(cont.split()[0]))
            list2.append(int(cont.split()[1]))
    print(list1)
    list1.sort()
    list2.sort()
    print(list1)
    difference = 0
    for i in range(len(list1)):
        difference += abs(list2[i] - list1[i])
    print (difference)
