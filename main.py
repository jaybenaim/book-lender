import random
from datetime import datetime


class Book:
    on_shelf = []
    on_loan = []
    day = []
    borrowed = False
    genres = []
    all_books = []

    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, isbn: {self.isbn} "

    @classmethod
    # instantiate a Book
    def create(cls, title, author, genre, isbn):
        """ this will create a new book """
        new_book = Book(title, author, genre, isbn)
        cls.on_shelf.append(new_book)
        cls.genres.append(genre)
        cls.all_books.append(new_book)
        return new_book

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14  # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        day = f"{datetime.fromtimestamp(future_timestamp, tz=None).day}"
        month = f"{datetime.fromtimestamp(future_timestamp, tz=None).month}"
        year = f"{datetime.fromtimestamp(future_timestamp, tz=None).year}"
        cls.string = f" Current Due Date {month}/{day}/{year}"

        return cls.string

    @classmethod
    def overdue_books(cls):
        due_date = cls.current_due_date()
        time_now = datetime.now()
        overdue_book = []
        for book in cls.on_loan:
            if due_date < datetime.now():
                overdue_book.append(book)
                if len(overdue_book) == 0:
                    return overdue_book
        return overdue_book

    @classmethod
    def browse(cls):
        """ this is how new books are added to the library """
        if cls.on_shelf != []:
            random_book = random.choice(cls.on_shelf)
            return random_book
        else:
            return "There are no books on the shelf, come back tomorrow"

    @classmethod
    def browse_genres(cls):
        if cls.genres != []:
            random_genre = random.choice(cls.genres)
            return random_genre

    @classmethod
    def search(cls, title, author, isbn):
        for book_title in cls.all_books:
            if book_title.title == title:
                return f"Yes we carry {book_title}"
            elif book_title.author == author:
                return f"Yes we carry {book_title}"
            elif book_title.isbn == isbn:
                return f"Yes we carry {book_title}"
            else:
                return f"Sorry, we dont carry that."

    # @classmethod
    # def search_author(cls, author)::
    #     for book_title in cls.all_books:
    #         if book_title.title == title:
    #             return f'Yes we carry {book_title}'
    #         else:
    #             return f'Sorry, we dont carry that.'
    # @classmethod
    # def search_isbn(cls, isbn):
    #     for book_title in cls.all_books:
    #         if book_title.title == title:
    #             return f'Yes we carry {book_title}'
    #         else:
    #             return f'Sorry, we dont carry that.'

    def borrow(self):
        """ This instance method is how a book is taken out of the library.
        This method should use lent_out to check if the book is already on loan,
        and if it is this method should return False to indicate that the attempt
        to borrow the book failed. Otherwise, use current_due_date to set the due_date
        of the book and move it from the collection 
        of available books to the collection of books on loan, then return True. """

        if self.lent_out() == True:
            return f"The Book is already out on loan."
        elif self.lent_out() == False:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True

    def return_to_library(self):
        """This instance method is how a book gets returned to the library.
         It should call lent_out to verify that the book was actually on loan.
          If it wasn't on loan in the first place, return False. 
          Otherwise, move the book from the collection of books on loan to the 
          collection of books on the library shelves, 
          and set the book's due date to None before returning True."""
        if self.lent_out() == False:
            return False
        else:
            self.on_loan.remove(self)
            self.on_shelf.append(self)
            date = self.current_due_date()
            date = None
            return True

    def lent_out(self):
        if self in Book.on_shelf:
            return False
        else:
            return True

    @classmethod
    def renew(cls):

        if cls.borrowed == False:
            now = datetime.now()
            two_weeks = 60 * 60 * 24 * 14  # two weeks expressed in seconds
            future_timestamp = now.timestamp() + two_weeks * 2
            day = f"{datetime.fromtimestamp(future_timestamp, tz=None).day}"
            month = f"{datetime.fromtimestamp(future_timestamp, tz=None).month}"
            year = f"{datetime.fromtimestamp(future_timestamp, tz=None).year}"
            cls.string = f" New Due Date {month}/{day}/{year}"
            Book.borrowed = True
            return cls.string
        if cls.borrowed == True:
            return "You cannot renew this book again"


sister_outsider = Book.create(
    "Sister Outsider", "Audre Lorde", "fiction", "9781515905431"
)
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "fiction", "9780896081307")
if_they_come = Book.create(
    "If They Come in the Morning", "Angela Y. Davis", "non-fiction", "0893880221"
)


# print(Book.browse().title)
# Book.browse().title  # "Ain't I a Woman?" (this value may be different for you)
# len(Book.on_shelf)  # 3
# len(Book.on_loan)  # 0
# sister_outsider.lent_out()  # False
# sister_outsider.borrow()  # True #######
# len(Book.on_shelf)  # 2
# len(Book.on_loan)  # 1 ######
# sister_outsider.lent_out()  # True
# print(sister_outsider.borrow())  # False
# print(sister_outsider.current_due_date())
# print(sister_outsider.renew())
# print(sister_outsider.renew())
# print(Book.browse_genres())
# print(sister_outsider.current_due_date())
# print(len(Book.overdue_books()))  # 0
# print(sister_outsider.return_to_library())  # True
# print(sister_outsider.lent_out())  # False
# print(len(Book.on_shelf))  # 3
# print(len(Book.on_loan))  # 0
print(Book.search(None, "Audre Lorde", None))  # fuzzy search ?
print(Book.search("Sister Outsidersas", None, None))
