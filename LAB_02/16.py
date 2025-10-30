class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "available":
                    book.status = "borrowed"
                    print(f"You borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "borrowed":
                    book.status = "available"
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")
    def list_available(self):
        print("\nAvailable books:")
        available = [book for book in self.books if book.status == "available"]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(f" - {book.title} by {book.author}")

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_available()

library.borrow_book("1984")
library.borrow_book("1984")  
library.return_book("1984")

library.list_available()