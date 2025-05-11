from Classes import *
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
choose = 0
new_session = Session()
system = SystemManger()
log_out_Admin = True
log_out_Customer = True
clear_screen()
while True:
    showlist1()
    choose = int(input())
    if choose == 1:
        print("To Sign Up Please Enter your Username, Password and Role[Admin or Customer] in same line")
        username, password, Role = input().split()
        system.sign_up(username, password, Role)
        print("Successful Sign UP")
        input("press Enter to move to home page")
        clear_screen()
        # break

    elif choose == 2 :
        username = input("Please Enter Username: ")
        password = input("Please Enter Password: ")
        result1, result2 = system.check(username, password) 
        if result1 :
            if result2 == 'Admin':
                while log_out_Admin :
                    showlist_Admin()
                    admin_choose = int(input())
                    if admin_choose == 1 :
                        print('Enter ID , Book name, Author and Total Page in same line')
                        id_str, book_name, author, total_page_str = input().split()
                        id, total_page = int(id_str), int(total_page_str)
                        admin = Admin()
                        admin.add_book(id, book_name, author, total_page)
                        print('The Process Success')
                        input("press Enter to move to home page")
                        clear_screen()

                    elif admin_choose == 2:
                        id = int(input("please enter Book ID : "))
                        admin.delete_book(id)
                        input("press Enter to move to home page")
                        clear_screen()

                    elif admin_choose == 3:
                        print("you now view all book")
                        system.view_all_book()
                        input("press Enter to move to home page")
                        clear_screen()
                    else:
                        print("you now logout")
                        log_out_Admin = False
                        input("press Enter to move to home page")
                        clear_screen()
                        break

            else:
                while log_out_Customer:
                    input("press Enter to move to home page")
                    clear_screen()
                    showlist_Customer()
                    customer_choose = int(input())
                    if customer_choose == 1:
                        print("this is view customer")
                        system.view_all_book()

                    elif customer_choose == 2:
                        print("this is Start Reading")
                        pre_book_id = int(input('Enter Book ID You Want To Read :'))
                        
                    elif customer_choose == 3:
                        print("this is View history")

                    else:
                        print("log out")
                        log_out_Customer = False
            
