class library:

    def __init__(self, list_of_books,name):
        self.booklist = list_of_books
        self.namee = name
        self.lendDict = {}

        def displayBooks(self):
            print(f"we have the following books in our library : {self.name}")
            for book in self.booksList:
                print(book)

        def lendBook(self,user,book):
            if book not in self.bookList:
                print("sorry , we do not have that book. get outta here")
            elif book in self.lendDict:
                print(f"the book us aldready being used by {self.lendDict[book]} . get outta here")
            else:
                self.lenDict[book] = user
                print(
                    "lender-book database has been updated. take the book and get outta here"
                )

        def addBook(self,book):
            self.bookList.append(book)
            print(f"{book} has been added to the book list")

        def returnBook(self,book):
            if book in self.lendDict:
                del self.lendDict[book]
                print("book has been returned. now getoutta here")
            else:
                print("that book wasn't borrowed from us")