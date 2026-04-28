# Merging two dictionaries into one dictionary
dict1 = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
dict2 = {'x' : 10, 'y' : 30, 'a' : 20}
dict3 = {}
for key in dict1:
    if key in dict2:
        val = dict1[key] + dict2[key]
        dict3.update({key : val})
    else:
        dict3.update({key : dict1[key]})
for key in dict2:
    if key not in dict1:
        dict3.update({key : dict2[key]})
print("Merging two dictionaries : ", dict3)