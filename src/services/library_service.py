import json
from src.models.book import Book
from src.models.member import Member


class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    # -----------------------------
    # SAVE & LOAD
    # -----------------------------
    def save_data(self):
        data = {
            "books": [
                {
                    "book_id": b.book_id,
                    "title": b.title,
                    "author": b.author,
                    "quantity": b.quantity
                }
                for b in self.books.values()
            ],
            "members": [
                {
                    "member_id": m.member_id,
                    "name": m.name,
                    "borrowed_books": m.borrowed_books
                }
                for m in self.members.values()
            ]
        }

        with open("data.txt", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open("data.txt", "r") as f:
                data = json.load(f)

                for b in data["books"]:
                    book = Book(b["book_id"], b["title"], b["author"], b["quantity"])
                    self.books[book.book_id] = book

                for m in data["members"]:
                    member = Member(m["member_id"], m["name"])
                    member.borrowed_books = m["borrowed_books"]
                    self.members[member.member_id] = member
        except:
            pass

    # -----------------------------
    # BOOK MANAGEMENT
    # -----------------------------
    def add_book(self, book):
        self.books[book.book_id] = book
        self.save_data()
        return "Book added successfully"

    def list_books(self):
        return list(self.books.values())

    def search_book(self, title):
        return [b for b in self.books.values() if title.lower() in b.title.lower()]

    # -----------------------------
    # MEMBER MANAGEMENT
    # -----------------------------
    def register_member(self, member):
        self.members[member.member_id] = member
        self.save_data()
        return "Member registered successfully"

    def list_members(self):
        return list(self.members.values())

    def get_member_books(self, member_id):
        if member_id not in self.members:
            return "Member not found"
        return self.members[member_id].borrowed_books

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
            self.save_data()
            return "Book borrowed successfully"
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
            self.save_data()
            return "Book returned successfully"
        return "This book was not borrowed"