class Book:
    """"A class to reperesent a book in a library."""

    def __init__(self, title, author):
        """Initialize the book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:
    """A class to manage a collection of books in library."""
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []
    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
    def check_out_book(self, title):
        """"Check out a book by its title, if available."""
        for book in self.books:
            if book.title == title:
                if book.check_out():
                    print(f"The book '{title}' has been checked out")
                    return
                else:
                    print(f"The book '{title}' is already checked out.")
                    return
        print(f"The book '{title}' is not in the library.")
    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                    return
                else:
                    print(f"The book '{title}' was not checked out.")
                    return
        print(f"The book '{title}' is not in the library.")
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else: 
            print("No books are currently available.")
                
