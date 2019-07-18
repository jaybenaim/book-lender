import random 
from datetime import datetime

class Book: 
    on_shelf = [] 
    on_loan = [] 

    def __init__(self, title, author, ISBN): 
        self.title = title 
        self.author = author 
        self.ISBN = ISBN 
    def __str__(self): 
        return f'{self.title} by {self.author}, ISBN: {self.ISBN} '
    @classmethod 
    # instantiate a Book 
    def create(cls, title, author, ISBN):
        ''' this will create a new book '''   
        new_book = Book(title, author, ISBN)
        cls.on_shelf.append(new_book) 
        return new_book 

    @classmethod 
    def current_due_date(cls): 
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp) 
    @classmethod 
    def overdue_books(cls): 
        due_date = cls.current_due_date()
        time_now = datetime.now()
        overdue_book = [] 
        for book in cls.on_loan: 
            # if current due date is 
            if (due_date > time_now) == True: 
        #         return book 
                overdue_book.append(book)
                if len(overdue_book) == 0: 
                    return overdue_book 

        return overdue_book

    @classmethod
    def browse(cls): 
        ''' this is how new books are added to the library ''' 
        if cls.on_shelf != []: 
            random_book = random.choice(cls.on_shelf) 
            return random_book
        else: 
            return 'There are no books on the shelf, come back tomorrow'

    def borrow(self): 
        ''' This instance method is how a book is taken out of the library.
        This method should use lent_out to check if the book is already on loan,
        and if it is this method should return False to indicate that the attempt
        to borrow the book failed. Otherwise, use current_due_date to set the due_date
        of the book and move it from the collection 
        of available books to the collection of books on loan, then return True. '''
        if self.lent_out() == True: 
            return False 
        elif self.lent_out() == False: 
            self.on_loan.append(Book)
            return True 
        else: 
            self.current_due_date() 
            self.on_loan.append(Book)
            return True 

    def return_to_library(self): 
        '''This instance method is how a book gets returned to the library.
         It should call lent_out to verify that the book was actually on loan.
          If it wasn't on loan in the first place, return False. 
          Otherwise, move the book from the collection of books on loan to the 
          collection of books on the library shelves, 
          and set the book's due date to None before returning True.'''
        if self.lent_out() == False: 
              return False  
        else: 
            self.on_shelf.append(Book)
            date = self.current_due_date() 
            date = None 
            return True 

    def lent_out(self): 
        for book in Book.on_shelf: 
            if book == self.title: 
                # if the book is on the shelf and available for rent 
                return True 
            else: 
                # if the book lent out 
                return False   
            
sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False

print(sister_outsider.borrow()) # True #######


print(len(Book.on_shelf)) # 2

print(len(Book.on_loan)) # 1 ###### 
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.current_due_date()) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue_books())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0