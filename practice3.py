class Book:
    def __init__(self, title, author, isbn, available=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        if self.available is None:
            self.available = True

    def __str__(self) -> str:
        return(
              f' title : {self.title}\n'
              f' author : {self.author}\n'
              f' isbn : {self.isbn}\n'
              f' available : {self.available}\n'
            )
    
    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True




class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        if self.borrowed_books is None:
            self.borrowed_books = []
    def __str__(self) -> str:
        return(
            f' ID = {self.member_id}\n'
            f' name = {self.name}\n'
        )
    
    def str_borrowed_book(self):
        for i in self.borrowed_books:
            print(i.isbn)

    def borrowed_book(self, book:Book):
        self.borrowed_books.append(book)
        book.borrow()
        

    def return_book(self, book:Book):
        self.borrowed_books.remove(book)
        book.return_book()

        


class Library:
    def __init__(self, books=None, members=None):
        self.books = books
        self.members = members
        if self.books is None:
            self.books = []
        if self.members is None:
            self.members = []

    def str(self) -> str:
        for i in self.books:
            print (i)

        for i in self. members:
            print(i)

    def add_book(self, book:Book):
        self.books.append(book)

    def register_member(self,member:Member):
        self.members.append(member)

    def issue_book(self, member_id, isbn):
        for m in self.members:
            if m.member_id == member_id:
                for b in self.books:
                    if b.isbn == isbn:
                        m.borrowed_book(b)

    def return_book(self,member_id, isbn):
        for m in self.members:
            if m.member_id == member_id:
                for b in self.books:
                    if b.isbn == isbn:
                        m.return_book(b)


# ایجاد کتاب‌ها
book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")

# ایجاد کتابخانه و اضافه کردن کتاب‌ها
library = Library()
library.add_book(book1)
library.add_book(book2)

# ثبت یک عضو
member = Member("آلیس", "M001")
library.register_member(member)

# امانت دادن کتاب به عضو
library.issue_book("M001", "1234567890")

# بازگرداندن کتاب
library.return_book("M001", "1234567890")

# library.str()
# member.str_borrowed_book()

