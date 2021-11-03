txt = "#ik hou van #frikandellen #ik en #wij hebben #ook #frikandellen. #ik"
x = txt.split("#")

list1 = []
list2 = []
def count(list1, c):
    return list1.count(c)

i = 1
while i < len(x):
    y = (x[i].split(" "))
    

    list1.append(y[0])
    z = count(list1, y[0])

    if (y[0], z-1) in list2:
        list2.remove((y[0], z-1))
        list2.append((y[0], z))
    else:
        list2.append((y[0], z))
    
    i += 1
    
print(list2)

