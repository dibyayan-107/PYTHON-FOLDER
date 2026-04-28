# list to dictionary conversion
my_dict = {}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
for x in range(0, len(keys)):
    for y in range(0, len(values)):
        if x == y:
            my_dict.update({keys[x]: values[y]})
        else:
            continue
print(my_dict)