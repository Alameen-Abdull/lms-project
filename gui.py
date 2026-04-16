import tkinter as tk
from tkinter import messagebox
from src.services.library_service import LibraryService
from src.models.book import Book
from src.models.member import Member

service = LibraryService()


# -----------------------------
# STYLES
# -----------------------------
BG_COLOR = "#1e1e2f"
FG_COLOR = "#ffffff"
BTN_COLOR = "#4CAF50"
FONT = ("Arial", 11)


# -----------------------------
# LIBRARIAN PANEL
# -----------------------------
def librarian_gui():
    win = tk.Toplevel()
    win.title("Librarian Panel")
    win.geometry("450x550")
    win.configure(bg=BG_COLOR)

    tk.Label(win, text="Librarian Panel", font=("Arial", 16, "bold"),
             bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

    def add_book():
        try:
            book = Book(int(b_id.get()), title.get(), author.get(), int(qty.get()))
            messagebox.showinfo("Success", service.add_book(book))
        except:
            messagebox.showerror("Error", "Invalid input")

    def view_books():
        books = service.list_books()
        if not books:
            messagebox.showinfo("Books", "No books available")
            return

        output = "\n".join(
            f"{b.book_id} | {b.title} | {b.author} | Qty:{b.quantity}"
            for b in books
        )
        messagebox.showinfo("Books", output)

    def register_member():
        try:
            member = Member(int(m_id.get()), m_name.get())
            messagebox.showinfo("Success", service.register_member(member))
        except:
            messagebox.showerror("Error", "Invalid input")

    # Inputs
    for text in ["Book ID", "Title", "Author", "Quantity"]:
        tk.Label(win, text=text, bg=BG_COLOR, fg=FG_COLOR).pack()
        if text == "Book ID":
            global b_id
            b_id = tk.Entry(win)
            b_id.pack()
        elif text == "Title":
            global title
            title = tk.Entry(win)
            title.pack()
        elif text == "Author":
            global author
            author = tk.Entry(win)
            author.pack()
        elif text == "Quantity":
            global qty
            qty = tk.Entry(win)
            qty.pack()

    tk.Button(win, text="Add Book", bg=BTN_COLOR, command=add_book).pack(pady=5)
    tk.Button(win, text="View Books", bg=BTN_COLOR, command=view_books).pack(pady=5)

    tk.Label(win, text="Member ID", bg=BG_COLOR, fg=FG_COLOR).pack()
    global m_id
    m_id = tk.Entry(win)
    m_id.pack()

    tk.Label(win, text="Member Name", bg=BG_COLOR, fg=FG_COLOR).pack()
    global m_name
    m_name = tk.Entry(win)
    m_name.pack()

    tk.Button(win, text="Register Member", bg=BTN_COLOR, command=register_member).pack(pady=10)


# -----------------------------
# STUDENT PANEL
# -----------------------------
def student_gui():
    win = tk.Toplevel()
    win.title("Student Panel")
    win.geometry("400x450")
    win.configure(bg=BG_COLOR)

    tk.Label(win, text="Student Panel", font=("Arial", 16, "bold"),
             bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

    def view_books():
        books = service.list_books()
        if not books:
            messagebox.showinfo("Books", "No books available")
            return

        output = "\n".join(
            f"{b.book_id} | {b.title} | Qty:{b.quantity}"
            for b in books
        )
        messagebox.showinfo("Books", output)

    def borrow():
        try:
            result = service.borrow_book(int(m_id.get()), int(b_id.get()))
            messagebox.showinfo("Borrow", result)
        except:
            messagebox.showerror("Error", "Invalid input")

    def return_book():
        try:
            result = service.return_book(int(m_id.get()), int(b_id.get()))
            messagebox.showinfo("Return", result)
        except:
            messagebox.showerror("Error", "Invalid input")

    tk.Label(win, text="Member ID", bg=BG_COLOR, fg=FG_COLOR).pack()
    global m_id
    m_id = tk.Entry(win)
    m_id.pack()

    tk.Label(win, text="Book ID", bg=BG_COLOR, fg=FG_COLOR).pack()
    global b_id
    b_id = tk.Entry(win)
    b_id.pack()

    tk.Button(win, text="View Books", bg=BTN_COLOR, command=view_books).pack(pady=5)
    tk.Button(win, text="Borrow Book", bg=BTN_COLOR, command=borrow).pack(pady=5)
    tk.Button(win, text="Return Book", bg=BTN_COLOR, command=return_book).pack(pady=5)


# -----------------------------
# MAIN WINDOW
# -----------------------------
def main():
    root = tk.Tk()
    root.title("Library System")
    root.geometry("300x250")
    root.configure(bg=BG_COLOR)

    tk.Label(root, text="Library System", font=("Arial", 16, "bold"),
             bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)

    tk.Button(root, text="Librarian", bg=BTN_COLOR, width=20,
              command=librarian_gui).pack(pady=10)

    tk.Button(root, text="Student", bg=BTN_COLOR, width=20,
              command=student_gui).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()