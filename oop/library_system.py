class Book:
    def __init__(self, title, author):
        """Initialize a Book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook with title, author and file size in KB.
        Calls the base class __init__ for title and author.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook with title, author and page count.
        Calls the base class __init__ for title and author.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.
        
        :param book: Instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)