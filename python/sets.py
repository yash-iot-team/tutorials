""" Sets are same that of list but excluding the following
its immutable but you can add and remove
each element needs to be unique
cannot modify individual items """

list4 = [1,2,3,4,5,6,4]
print('List4', list4)
set1= set(list4)
print('Set1', set1)
print('Type of Set1', type(set1))

set2 = {11,2,45,7,8,9,2}
print('Set2', set2)

set2.add(999)
print('Set2', set2)

set2.remove(11)
print('Set2', set2)

print('Set1 intersection set2', set1.intersection(set2))
print('Set1 difference set2', set1.difference(set2))
print('Set1 difference set2', set1.union(set2))
print('Set1 poping', set1.pop())
print('Set1 clearing', set1.clear())


# Immutable
set1[1] = 13
print('Set1', set1)


# Frozen Sets
print('*********************************************************')
# Fronzen set does not allow to add or remove

