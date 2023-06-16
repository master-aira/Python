# Create a Library Class
# Functions are - Display Book , Lend Book[Tell where to get if not Available] , Add Book , Return Book
# HarryLibrary - Library(List of Books , Library Name)
# Dictionary - Kisne Konsi Book li hai
#Create a main function and run an infinite while loop that asks the user for input to Perform the above Functions
class Library:
    def __init__(self,list_books,library_name):
        self.bookslist = list_books
        self.namelib = library_name
        self.lenddic = {}
    def Display(self):
        print(f"We have the following books in our library {self.namelib}")
        for Book in self.bookslist:
            print(Book)
    def Lend(self,user,Book):
        if Book not in self.lenddic.keys():
            self.lenddic.update({Book,user})
            print("Book Dictionary has been updated!!")
        else:
            print(f"This is already lend by {self.lenddic[Book]}")
    def Add(self,Book):
        self.bookslist.append(Book)
        print("Book has been added successfully")
    def Return(self,Book):
        self.bookslist.remove(Book)
        print("Thik hai Jao")
if __name__ == '__main__':
    harry = Library(["Python","C++","C#","Java"],"Bhut Achha Library")
while True:
    print("Aao Beta Kaise aana hua")
    i = input("Kya Kaam hai\n Dekhna hai\n Lend Karna hai\n Add Karna hai\n Return Karna hai\n")
    if i == "Display":
        harry.Display()
    elif i == "Lend":
        Book = input("Naam Batao Yaar Book ka")
        Name = input("Apna Naam Yaar")
        harry.Lend(Name,Book)
    elif i == "Add":
        Book = input("Naam Batao Yaar Book ka")
        harry.Add(Book)
    elif i == "Return":
       Book = input("Naam Batao Yaar Book ka")
       harry.Return(Book)
    else:
        print("Yeh sab nhi hota yha Khi aur Dekho")
    break