class Author:
    all_authors = []
    
    
    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)
        

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Book:
    all_books = []
    
    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]

    
class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Register this contract with the author and book
        author._contracts.append(self)
        book._contracts.append(self)

        # Track all contracts
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date=None):
        """Return contracts, optionally filtering by date."""
        if date:
            # Return only contracts that match the date
            return [c for c in cls.all if c.date == date]
        # Otherwise return all contracts sorted by date
        return sorted(cls.all, key=lambda c: c.date)