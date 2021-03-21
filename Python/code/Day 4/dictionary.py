# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

animals = {'cat' : 1, 'dog' : 10, 'horse': 3}
keys = animals.keys()

print(list(keys))

values = animals.values()
print(list(values))

animals.clear()

findkey = 'cat' in animals
print(findkey)





