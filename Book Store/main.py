""" Task: Build a Bookstore Application
You are tasked with creating a simple bookstore management application. The application will use a JSON file to store and manage book records.

Each book should have the following attributes:

ID (unique for each book)
Title
Author
Price
The application should support the following functionalities through methods in a class:

Add a Book: Add a new book to the store.
List All Books: Display all books in the store.
Delete a Book: Remove a book by its ID.
Update a Book: Modify details of a book using its ID. 

solution 
class book s constructor will contain all the books properties 
inside book class we will need a method to add books and another method to view books 

"""
import json

class Book:
    def __init__(self):
        ...

    def addbook(self,id,title,author,price):
        self.id = id 
        self.title = title
        self.author = author 
        self.price = price 

        addCount : int = int(input("Enter the number of books that you want to add: "))
        for bookCount in range(addCount):
            id : int = int(input("Enter the book's ID: "))
            title : string = input("Enter the book's TITLE: ")
            author : string = input("Enter the name of author: ")
            price : int = int(input("Enter the PRICE of the book: "))

            bookCollection[bookCount] = {
                "bookid" : id ,
                "booktitle": title,
                "bookauthor" : author,
                "bookprice" : price 
            }
            with open("data.json","a+") as file:
                json.dump(bookCollection[bookCount],file , indent=4)
        # totalbookcount += bookCount

    def viewbook(self):
        # for bookCount in range(totalbookcount):
        with open("data.json","r") as file:
                
                print(collection)

bookCollection = {}
# totalbookcount = 0

muna = Book()
muna.addbook(532,"Sapiens" , "Yuval Noah Harari", 500)
muna.viewbook() 