class Addition:                                        #Class 
    num1 = 1000                                        #class variable
    num2 = 2000
    num3 = 3000
    def result(self):                                  #Instance Method
       self.val = self.num1 + self.num2 + self.num3    #val is a instance variable
       print("Output : ", self.val)
sum = Addition()
print("First value : ",sum.num1)
print("Second value : ",sum.num2)
print("Third value : ",sum.num3)
sum.result()