class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False


    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book):
        self.books.append(book)


    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.checkout():
                    return f"{title} has been checked out."
                else:
                    return f"{title} is already checked out."
        return f"{title} not found in library"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    return f"{title} has been returned"
                else:
                    return f"{title} was not checked out."
        return f"{title} not found in library"


    def list_available_books(self):
        for book in self.books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
