# Tuple (immutable)
tp = (1, 2, 'bill', False)
print(tp, type(tp)) 

# acess 
# tp[0] = 'can\'t cause tpl immutaable'


# syntax 
'''
dict = {key : value}
'''
dict = {}
dict['name'] = 'Python'
dict['age'] = 16
print(dict['name'])

dict = {'bill': '8478754', 'steve': '7444'}
print(dict['bill'])


# iteration 
# key and value 
asci_dict = {'a': 97, 'b': 98, 'c':99, 'd':100}
# keys(), values(), items()
for key, value in asci_dict.items():
    print(key, value, sep=' -> ')

