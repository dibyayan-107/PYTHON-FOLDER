#Basic library management system (Mini project)
library = {}
sub_id = "#B"

#Checking the format of Book ID
def check_id(_id):
   if _id[:2] == sub_id and _id[2:].isdigit() == True:
      return True
   else:
      return False
#Printing the format rule of Book ID
def format_rule():
   print("<**Book id format should be like #B(int)**>")

#Adding book record in library
def add_book():
    format_rule()
    book_id = input("Enter book ID : ")
    if check_id(book_id):
        if book_id in library:
          print("This book already exists!!")
          return
        else:
            book_name = input("Enter title of the book : ")
            if book_name.isdigit():
               print("Invalid book name!")
               return    
            book_author = input("Enter author of the book : ")
            if book_author.isdigit():
               print("Invalid author name!")
               return
            try:
                book_quantity = int(input("Enter quantity : "))
                if book_quantity <= 0:
                  print("Enter only positive & non-zero value!")
                  return
            except ValueError:
               print("Invalid quantity!")
               return
            library.update({
            book_id : 
            {
             "title" : book_name, 
             "author" : book_author, 
             "quantity" : book_quantity
            }
            })
    else:
        print("This book id format is not valid!!")
        return
    print("Book added successfully in library!!")


#Deleting book record from library
def delete_book():
    format_rule()
    book_id = input("Enter book ID to delete : ")
    if check_id(book_id):
      if book_id not in library:
         print("Sorry!This book doesn't exist in library!!")
      else:
         library.pop(book_id)
         print("The record of the Book is deleted successfully from library!!") 
    else:
       print("This book id format is not valid!!")   


#Issuing book from library
def issue_book():
    format_rule()
    book_id = input("Enter book ID to issue : ")
    if library == {}:
       print("Oops! Book record is empty!!")
       return
    if check_id(book_id):
      if book_id in library:
           if library[book_id]["quantity"] == 0:
             print("Sorry!This book is out of stock!!")
             return
           else:
             library[book_id]["quantity"] -= 1
             print("Book issued successfully!!")
      else:
        print("Sorry!This book doesn't exist in library!!")
        return
    else:
      print("This book id format is not valid!!")
      return


#Returning book to the library
def return_book():
    format_rule()
    book_id = input("Enter book ID to return : ")
    if library == {}:
       print("Oops! Book record is empty!!")
       return
    if check_id(book_id):
       if book_id not in library:
         print("Sorry!This book is never issued!!")
       else:
         library[book_id]["quantity"] += 1
         print("Book returned successfully!!")
    else:
        print("This book id format is not valid!!")
        return


#Searching a particular book in library
def search_book():
    format_rule()
    if library == {}:
       print("Oops! Book record is empty!!")
       return
    x = input("Are you want to search a book by ID/Name?(I/N) : ")
    if x == "I" or x == "i":
        book_id = input("Enter book ID to search : ")
        if check_id(book_id):
          if book_id in library:
              print("The book is found!!")
              print("Book name : ", library[book_id]["title"])
              print("Book's author : ", library[book_id]["author"])
          else:
              print("Sorry!The book is not found!!")
        else:
           print("This book id format is not valid!!")
           return
    elif x == "N" or x == "n":
        flag = 0
        book_name = input("Enter book name to search : ")
        for key in library.keys():
            if library[key]["title"].lower() == book_name.lower():
                print("The book is found!!")
                print("Book name : ", library[key]["title"])
                print("Book's author : ", library[key]["author"])
                flag = 1
                break
        if flag != 1:
            print("Sorry!The book is not found!!")
            return
    else:
       print("Invalid Choice!")
               
       
    

#Displaying all book record from library
def display():
    if library == {}:
        print("Nothing to show!! Book record is empty!!")
    else:
        print(f"\nLibrary store :- \n")
        for book_id in library.keys():
             print(f"Book Id : {book_id}")
             print(f"Book name : {library[book_id]['title']}")
             print(f"Book's author name : {library[book_id]['author']}")
             print(f"Quantity : {library[book_id]['quantity']}")
             print("\n")


choice = 0
while True:
    print("\tMenu\t\n1.<Add book>\n2.<Delete book>\n3.<Issue book>\n4.<Return book>\n5.<Search book>\n6.<Display>\n7.<Exit>")
    try:
     choice = int(input("Enter your choice : "))
     if choice == 1:
         add_book()
     elif choice == 2:
         delete_book()
     elif choice == 3:
         issue_book()
     elif choice == 4:
         return_book()
     elif choice == 5:
         search_book()
     elif choice == 6:
         display()
     elif choice == 7:
         break
     else:
         print("Invalid choice!!")
    except ValueError:
        print("Your choice must be in integer format!!")