l = [1,2,3, "Umang", True]
print(type(l))
print(l)


# below both are same

print(l[-3])
print(l[len(l)-3])

if 1 in l:
    print("Yes")
    
lst = [i for i in range(4)]
# print 0 , 1, 2, 3
print(lst)