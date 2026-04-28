#Library management system(Mini project)
library = {}
sub_id = "#B"

#Adding book record in library
def add_book():
    print("<**Book id format should be like #B___**>")
    book_id = input("Enter book id : ")
    if book_id[:2] == sub_id:
       if book_id in library:
          print("This book is already exist!!")
          return
       else:
          book_name = input("Enter tittle of the book : ")
          book_author = input("Enter author of the book : ")
          book_quantity = int(input("Enter quantity : "))
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
    print("<**Book id format should be like #B___**>")
    book_id = input("Enter book id to delete : ")
    if book_id[:2] == sub_id:
      if book_id not in library:
         print("Sorry!This book doesn't exist in library!!")
      else:
         library.pop(book_id)
         print("The record of the Book deleted successfully from library!!") 
    else:
       print("This book id format is not valid!!")   


#Issuing book from library
def issue_book():
    print("<**Book id format should be like #B___**>")
    book_id = input("Enter book id to issue : ")
    if book_id[:2] == sub_id:
      if book_id in library:
           if library[book_id]["quantity"] == 0:
             print("Sorry!This book is out of stock!!")
             return
           else:
             library[book_id]["quantity"] -= 1
             print("Book issued successfully!!")
      else:
        print("Sorry!This book doesn't exist in library!!")
    else:
      print("This book id format is not valid!!")


#Returning book to the library
def return_book():
    print("<**Book id format should be like #B___**>")
    book_id = input("Enter book id to return : ")
    if book_id[:2] == sub_id:
       if book_id not in library:
         print("Sorry!This book is never issued!!")
       else:
         library[book_id]["quantity"] += 1
         print("Book returned successfully!!")
    else:
        print("This book id format is not valid!!")


#Searching a particular book in library
def search_book():
    print("<**Book id format should be like #B___**>")
    book_id = input("Enter book id to search : ")
    if book_id[:2] == sub_id:
      if book_id in library:
        print("The book is found!!")
        print("Book name : ", library[book_id]["title"])
        print("Book's author : ", library[book_id]["author"])
      else:
        print("Sorry!But the book is not found!!")
    else:
        print("This book id format is not valid!!")


#Displaying all book record from library
def display():
    if library == {}:
        print("Nothing to show!! All book sets are empty!!")
    else:
        print(f"Library store :- \n")
        for book_id in library.keys():
             print(f"Book Id : {book_id}")
             print(f"Book name : {library[book_id]["title"]}")
             print(f"Book's author name : {library[book_id]["author"]}")
             print(f"Quantity : {library[book_id]["quantity"]}")
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
         print("Your choice is not valid!!")
    except ValueError:
        print("Your choice must be in integer format!!")