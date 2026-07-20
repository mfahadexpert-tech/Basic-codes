# ==============================
# Book Class
# ==============================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True

    # Getter
    def get_availability(self):
        return self.__is_available

    # Setter
    def set_availability(self, status):
        if isinstance(status, bool):
            self.__is_available = status
        else:
            print("Invalid Availability Status")

    def display_book(self):
        print("\nBook Title :", self.title)
        print("Author     :", self.author)
        print("Available  :", self.__is_available)


# ==============================
# Library Class (Aggregation)
# ==============================

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} Added Successfully.")

    def show_books(self):
        print("\nBooks in Library")
        print("---------------------------")

        if len(self.books) == 0:
            print("No Books Available")
        else:
            for book in self.books:
                status = "Available" if book.get_availability() else "Issued"
                print(f"{book.title} by {book.author} --> {status}")


# ==============================
# Parent Class
# ==============================

class LibraryMember:
    def __init__(self, name):
        self.name = name

    def borrow_limit(self):
        return 0

    def borrow_book(self, book):

        if book.get_availability():
            book.set_availability(False)
            print(f"{self.name} borrowed '{book.title}'")
            print("Book Issued")
        else:
            print("Out of Stock")


# ==============================
# Child Class
# ==============================

class StudentMember(LibraryMember):

    def borrow_limit(self):
        return 2


# ==============================
# Child Class
# ==============================

class TeacherMember(LibraryMember):

    def borrow_limit(self):
        return 5


# ==============================
# Testing
# ==============================

book1 = Book("Python Programming", "Ali Raza")
book2 = Book("Data Structures", "Ahmed Khan")

library = Library("City Library")

library.add_book(book1)
library.add_book(book2)

library.show_books()

student = StudentMember("Fahad")
teacher = TeacherMember("Usman")

print("\nStudent Borrow Limit :", student.borrow_limit())
print("Teacher Borrow Limit :", teacher.borrow_limit())

student.borrow_book(book1)

teacher.borrow_book(book1)

teacher.borrow_book(book2)

library.show_books()

book1.display_book()
book2.display_book()