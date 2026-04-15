from src.services.library_service import LibraryService
from src.models.book import Book
from src.models.member import Member


def test_add_book():
    service = LibraryService()
    book = Book(1, "Python Basics", "John Doe", 5)

    service.add_book(book)

    assert 1 in service.books


def test_register_member():
    service = LibraryService()
    member = Member(1, "Ali")

    service.register_member(member)

    assert 1 in service.members


def test_borrow_book():
    service = LibraryService()

    book = Book(1, "Python", "John", 2)
    member = Member(1, "Ali")

    service.add_book(book)
    service.register_member(member)

    result = service.borrow_book(1, 1)

    assert result == "Book borrowed successfully"
def test_return_book():
    service = LibraryService()

    book = Book(1, "Python", "John", 1)
    member = Member(1, "Ali")

    service.add_book(book)
    service.register_member(member)

    service.borrow_book(1, 1)
    result = service.return_book(1, 1)

    assert result == "Book returned successfully"    