from audioop import reverse


list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
print('List1 Element: ', list1)

print('Length of list : ', len(list1))
print('Index 0th : ', list1[0])
print('Index -1th : ', list1[-1])


list1[1] = "IoT Core"
print('List1 Element: ', list1)


# Methods supported in List
list2 = [1,2,3,4,5,6,7,8,9,0]
print('Min Val in List : ', min(list2))
print('Max Val in List : ', max(list2))
#print('Max Val in List : ', max(list1)) # Will throw error considering both strings and numbers are in same list

list1.append(100) # adding element to list in the last index
print('List1 Element: ', list1)
print('List1 Element: ', list1.pop(0)) # returns el 0 from the list and deletes it from list

del list1[len(list1)-1] # deletes a element
print('List1 Element: ', list1)


list1.remove('IoT Core')
print('List1 Element: ', list1)

list1.insert(0, 'IoT Core')
print('List1 Element: ', list1)

list1.extend(list2) # adds list2 to list1
print('List1 Element: ', list1)

list1.append(10)
print('List1 Element: ', list1)

print('Count List1 for 10 in Elements: ', list1.count(10))
print('List2 : ', list2)


# List sorting not working as expected

list3= [23,65,1,46,999, 567]
print('List3 : ', list3)

list3.sort()
print('List3 Element Asc order: ', list3)

list3.reverse()
print('List3 Element Desc order: ', list3)

print('List3 Element Asc order: ', sorted(list3))
print('List3 Element Desc order: ', sorted(list3, reverse=True))

# Slicing
print('***************************************')
print('List3 : ', list3)

list3[0:2]
print('List3 Sliced: ', list3[0:2])




