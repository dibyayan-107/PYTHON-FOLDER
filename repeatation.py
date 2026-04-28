def first_unique_char(s):
    c = 0
    my_list = list(s)
    length = len(my_list)
    for val in my_list:
        n = my_list.count(val)
        if n == 1:
            c += 1
        else:
            break
    if c == length:
        print("All characters are unique!!")
        exit()
    for item in my_list:
        n = my_list.count(item)
        if n == 1:
            return item
        else:
            continue
    return None
my_str = input("Enter any string : ")
print("First non-repeating character : ", first_unique_char(my_str))

