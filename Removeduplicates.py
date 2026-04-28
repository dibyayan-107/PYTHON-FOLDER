list1 = []
list2 = []
n = int(input("How many elements you want to add? "))
for i in range(0, n):
    val = int(input("Enter data : "))
    list1.append(val)
print(f"Original list : {list1}")
index = 0
for i in range(0, n):
    count = 0
    for j in range(0, n):
      if j == i:
          continue
      elif list1[i] == list1[j]:
          count += 1
    if count == 0:
       list2.insert(index, list1[i])
       index += 1
print(f"After removing duplicate elements : {list2}")