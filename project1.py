# Student record management (mini project)
my_dict = {}                                         # Global variable

def Add_student():                                   # Function call to Add_student()
    name = input("Enter student name : ")
    if name in my_dict:
        print("This student name already exists!")
    else:
      try:
         marks = int(input("Enter student marks(%): "))
         my_dict.update({name : marks})
      except ValueError:
         print("Please enter digit only!!")


def Delete_student():                                 # Function call to Delete_student()
    s = input("Delete whole student record?(y/n) : ") 
    if s == 'y' or s == 'Y':
      if my_dict == {}:
        print("Nothing to delete because student record is empty!!")
      else:
        my_dict.clear()
        print("Student record is cleared successfully!")
    elif s == 'n' or s == 'N':
      key = input("Enter student name to delete : ")
      remove = my_dict.pop(key, None)
      if remove is None:
        print("Student name is not found!")
      else:
        print("Student name is deleted successfully!") 
    else:
      print("Invalid option!")


def Search_student():                                 # Function call to Search_student()
     name = input("Enter student name to search : ")
     if name in my_dict:
      print("Student is found in record!")
     else:
      print("Student is not found!")


def Display():  
   print("\n")                                      # Function call to Display_student()
   print("\t~Student Record~")   
   print(" | Student name  |   Marks(%) |")                      
   for x, y in my_dict.items():
      print(f"\t{x}\t\t{y}")
   print("\n")


choice = 0
while True:
    print("\tMenu\t\n1.Add student\n2.Delete student\n3.Search student\n4.Display\n5.Exit")
    try:
        choice = int(input("Enter your choice : "))
        if choice == 1:
           Add_student()
        elif choice == 2:
           Delete_student()
        elif choice == 3:
           Search_student()
        elif choice == 4:
           Display()
        elif choice == 5:
           print("Exiting program!...")
           break
        else:
           print("Invalid choice! try again!")

    except ValueError:
        print("Please enter digits only from 1 to 5!!")
    