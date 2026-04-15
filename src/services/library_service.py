from src.models.book import Book
from src.models.member import Member


class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}

    # -----------------------------
    # BOOK MANAGEMENT
    # -----------------------------
    def add_book(self, book):
        self.books[book.book_id] = book
        return "Book added successfully"

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return "Book removed successfully"
        return "Book not found"

    def list_books(self):
        return list(self.books.values())

    # -----------------------------
    # MEMBER MANAGEMENT
    # -----------------------------
    def register_member(self, member):
        self.members[member.member_id] = member
        return "Member registered successfully"

    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            return "Member removed successfully"
        return "Member not found"

    def list_members(self):
        return list(self.members.values())

    # -----------------------------
    # BORROWING SYSTEM
    # -----------------------------
    def borrow_book(self, member_id, book_id):
        if book_id not in self.books:
            return "Book not found"

        if member_id not in self.members:
            return "Member not found"

        book = self.books[book_id]
        member = self.members[member_id]

        if book.quantity > 0:
            book.quantity -= 1
            member.borrowed_books.append(book_id)
            return "Book borrowed successfully"
        else:
            return "Book not available"

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            return "Member not found"

        if book_id not in self.books:
            return "Book not found"

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id in member.borrowed_books:
            member.borrowed_books.remove(book_id)
            book.quantity += 1
            return "Book returned successfully"
        else:
            return "This book was not borrowed by the member"