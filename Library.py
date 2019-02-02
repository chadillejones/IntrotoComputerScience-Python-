# Library.py
# This class simulates a library. We can add books, check books out, return books, and check if the library currently has a given book.

# The class should be named Library.
# The __init__ method should take no arguments.
# There should be an add_book method that takes a string and records that the library has that book in stock.
# There should be a check_out_book method that takes a string and records that the book is checked out from the library.
# There should be a return_book method that takes a string and records that the library has that book in stock.
# There should be a has_book method that takes a string and returns True if that book is in stock at the library, and False if it is not.

# Example Code: (This code should work, and give the expected results, if your code is correct.

class Library():
    
    def __init__(self):
        self.books=[]
        
    def add_book(self,book):
        self.books.append(book)
        
    def check_out_book(self,book):
        self.books.remove(book)
        
    def return_book(self,book):
         self.books.append(book)
                
    def has_book(self,book):
        int_pholder=0
        for x in range(0,len(self.books)):
            if self.books[x]==book:
                print("True")
                return True
                int_pholder=1
        if int_pholder==0:
            print("False")
            return False
        

library = Library()
library.add_book("The Prince")
library.add_book("War and Peace")
library.check_out_book("The Prince")
library.has_book("The Prince") # False
library.has_book("War and Peace") # True
library.has_book("Les Miserables") # False
library.return_book("The Prince")
library.has_book("The Prince") # True
