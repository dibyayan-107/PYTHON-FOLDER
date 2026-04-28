# Menu driven dictionary program
my_dict = {}

def Add():
  key = input("Enter key to add : ")
  val = int(input("Enter value to add : "))
  my_dict.update({key : val})
  print(f"[{key} : {val}] added successfully!")

def Delete():
  s = input("Are you want to delete the whole dictionary?(y/n) : ") 
  if s == 'y' or s == 'Y':
    if my_dict == {}:
      print("Nothing to delete because dictionary is empty!!")
    else:
      my_dict.clear()
      print("Dictionary is cleared successfully!")
  elif s == 'n' or s == 'N':
    key = input("Enter key to delete : ")
    remove = my_dict.pop(key, None)
    if remove is None:
      print("Key is not found!")
    else:
      print("Key is deleted successfully!") 
  else:
    print("Invalid option!")

def Search():
  key = input("Enter key to search : ")
  if key in my_dict:
    print("Key is found in dictionary!")
  else:
    print("Key is not found!")

def Display():
  print(f"My dictionary : {my_dict}")

choice = 0
while True:
    print("\tMenu\t\n1. Add item\n2. Delete item\n3. Search item\n4. Display\n5. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
      Add()
    elif choice == 2:
      Delete()
    elif choice == 3:
      Search()
    elif choice == 4:
      Display()
    elif choice == 5:
      break
    else:
      print("Invalid choice!!")
