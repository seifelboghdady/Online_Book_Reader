class User:
    def __init__(self, user_name = None, password = None, role = None):
        self.id = 0
        self.user_name = user_name
        self.password = password
        self.Role = role
    
    def login(self, username, password):
        return self.user_name == username and self.password == password


    def logout(self):
        pass
#_________________________

class Admin(User):
    
    def add_book(self, id, Book_name, Author, total_page):
        SystemManger.books.append(Book(id, Book_name, Author, total_page))

    def delete_book(self, id):
        for book in SystemManger.books:
            if book.id == id:
                SystemManger.books.remove(book)
                print(f"Book with id {id} has been deleted.")
                break
        else:
            print(f"No book found with id {id}")       
#________________________
class Customer(User):
    def start_read(self):
        pass

    def Go_next_page(self):
        pass

    def Go_previous_page(self):
        pass

    def view_history(self):
        pass

class Book:
    def __init__(self, id, title, author, total_page):
        self.id = id
        self.title = title
        self.author = author
        self.total_page = total_page

from datetime import datetime
class Session:
    def __init__(self):
        self.session_id = 0
        self.book_id = 0
        self.current_page = 0
        self.timeTamp = datetime.now() 
import os
class SystemManger:
    users = []
    books = []
    def __init__(self):
        self.user_id_counter = 1
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def sign_up(self, username:str, password:str, role:str):
        if role == 'Admin':
            self.users.append(Admin(username, password, role))
        else:
            self.users.append(Customer(username, password, role))
        print("Successful Sign UP")

    # @classmethod
    def view_all_book(self): #(class method)
        for book in self.books:
            print(f"Name: {book.title}, Author: {book.author}")

    def check(self, username, password):
        for user in self.users:
            if user.login(username, password):
                return True, user.Role
        return False, None

    def find_user(self):
        pass

    
def showlist1():
    print("Hello to Online Book Reader\n1- Sign Up\n2- Log in\n3- Exit\nPlease Enter your Choose[1:3]")

def showlist_Admin():
    print('1- Add Book \n2- Delete Book\n3- View All Book \n4- Log Out [1:4]')

def showlist_Customer():
    print("1- View \n2- Start Reading \n3- View History Reading \n4- Log Out [1:4]")

# def check(system:SystemManger, username, password):
#     for user in system.users:
#         if user.login(username, password):
#             print("hello")
#             return [True, user.Role]
#     print("Username or Password uncorrected")
#     return [False, None]
