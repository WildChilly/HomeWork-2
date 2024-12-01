my_first_dict = mfd = {'Alexey': 'Bass guitar', 'Oleg': 'Sax', 'Anton': 'Trombone', 'Zheka': 'Drums', 'Kostya': 'Guitar', 'Jonathan':'Vocal', 'Sanya':'Sound Mixer'}
print(mfd)

print(mfd['Oleg'])
print(mfd.get('Karpenko'))
mfd.update({'Karpenko':'Ex Trombone', 'Artur':'Driver'})
print(mfd)
print(mfd.keys())
print(mfd.values())

uvolen_is_grupp = mfd.pop('Karpenko')

print(uvolen_is_grupp)
print(mfd)



#Множества
my_first_set = mfs = {1, 2, 2, 2, 'Ex Trombone', 'Ex Trombone', True, False, True}
print(mfs)
mfs.update({3,4})
print(mfs)
mfs.remove(2)
mfs.discard(True)
mfs.remove('Ex Trombone')
mfs.add(list[1,2,3,3,4,6])
mfs.add(list[True, True])
print(mfs)