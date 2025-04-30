my_dict = {'tuple': (1, 'text', False, 5, 2.5), 'list': [1, None, False, 25.1, 'test'],
           'dict': {'first': 'one', 'second': 'two', 'third': 'three', 'fourth': 'four', 'fifth': 'five'},
           'set': {1, None, False, 29, 1, 59, 'test2'}
           }
my_tuple = my_dict['tuple']
print('Ответ кортежа : ', my_tuple[-1])

my_list = my_dict['list']
my_list.append(42)
my_list.pop(1)
print('Ответ списка : ', my_list)

dict_2 = my_dict['dict']
dict_2[('i am a tuple',)] = ('six',)
dict_2.pop('second')
print('Ответ словаря : ', dict_2)

my_set = my_dict['set']
my_set.add(99)
my_set.remove(29)
print('Ответ множества : ', my_set)

print(my_dict)
