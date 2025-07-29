my_list = list()

for x in range(1,5):
    my_list.append(x*10)


my_list[1] = 15
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print(my_list.index(30))