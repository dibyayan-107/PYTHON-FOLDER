# class Addition:                                        #Class 
#     num1 = 1000                                        #class variable
#     num2 = 2000
#     num3 = 3000
#     def result(self):                                  #Instance Method
#        self.val = self.num1 + self.num2 + self.num3    #self.val is a instance variable
#        print("Output : ", self.val)
# sum = Addition()
# print("First value : ",sum.num1)
# print("Second value : ",sum.num2)
# print("Third value : ",sum.num3)
# sum.result()

class Book:
    def __init__(self, a, b, c, d):
          self.book_name = a
          self._book_id = b
          self.author = c
          self.quantity = d
    def book_details(self):
         print("Book name:- ",book_name)
         print("Book ID:- ",book_id)
         print("Book author name:- ",book_author)
         print("Quantity:- ",quantity)

book_name = input("Enter book name:- ")
book_id = input("Enter book ID:- ")
book_author = input("Enter author name:- ")
quantity = int(input("Enter quantity:- "))
B1 = Book(book_name, book_id, book_author, quantity)
B1.book_details()