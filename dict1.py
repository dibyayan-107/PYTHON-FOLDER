S = input("Enter string:- ")
my_dict = dict()
for item in S:
    if item not in my_dict:
        my_dict.update({item : 1})
    else:
        my_dict[item] += 1
print("Original:- ", my_dict)
m = dict()
for item in list(my_dict.items()):
    if item[1] != 1:
        m.update({item[0] : item[1]})
    else:
        continue
print("Dictionary with only duplicates:- ",m)