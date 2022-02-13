dict1 = {'vendor':'cisco','model':'asm100','status':'connected', 'ts':10356589 }
print('Dict1: ', dict1)
print('Length Dict1: ', len(dict1))

print('Dict1 accessing key vendor: ', dict1['vendor'])

dict1['vendor'] = 'ST Microtronics'
print('Dict1 accessing key vendor: ', dict1['vendor'])


print('is ts available in dict1 ', 'ts' in dict1)
del dict1['ts']
print('is ts available in dict1 ', 'ts' in dict1)
print('is ts available in dict1 ', 'ts' not in dict1)

print('Dict1: ', dict1)
print('Dict1 Keys: ', dict1.keys())
print('Dict1 Values: ', dict1.values())


print('Dict1 Items Tuples: ', dict1.items())


print('Type of Dict1: ', type(dict1.keys()))
print('Type of Dict1: ', type(dict1.values()))
print('Type of Dict1: ', type(dict1.items()))

print('List return of Dict1: ', list(dict1.keys()))
print('List return of Dict1: ', list(dict1.values()))
print('List return of Dict1: ', list(dict1.items()))

