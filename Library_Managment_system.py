from tabulate import tabulate
books={
    "shelf1":[101,102,103,104,105,106,107,108,109,110],
    "shelf2":[201,202,203,204,205,206,207,208,209,210],
    "shelf3":[301,302,303,304,305,306,307,308,309,310],
    "shelf4":[401,402,403,404,405,406,407,408,409,410],
    "shelf5":[501,502,503,504,505,506,507,508,509,510],
    "shelf6":[601,602,603,604,605,606,607,608,609,610],
    "shelf7":[701,702,703,704,705,706,707,708,709,710],
    "shelf8":[801,802,803,804,805,806,807,808,809,810],
    "shelf9":[901,902,903,904,905,906,907,908,909,910],
    "shelf10":[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
}
def display_books():
    headers = ["Shelf", "Books"]
    table = [(shelf, ", ".join(map(str, books[shelf]))) for shelf in books]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
print()
print()
while True:
    print()
    print()
    ans=int(input('''Enter 1 to display all books- \nEnter 2 to search for a book- 
    \nEnter 3 for issuing a book- \nEnter 4 to return a book- \nEnter 5 to exit- \n'''))
    if ans==1:
        display_books()
        
    elif ans==2:
        book=int(input("Enter the book number you want to search for: "))
        for i in books:
            if book in books[i]:
                print("Book is available in ",i)
                break
        else:
            print("Book is not available")
    elif ans==3:
        book=int(input("Enter the book number you want to issue: "))
        student_code=int(input("Enter your 6 digit student code: "))
        for i in books:
            if book in books[i]:
                print("Book is available in shelf",i)
                book_issued=books[i].remove(book)
                print("Book issued successfully")
                books[i].append(student_code)
                print(f"The book {book} has been issued to the student {student_code} ")    
                break
            else:
                 print("Book is not available")
    elif ans==4:
        book=int(input("Enter the book number you want to return: "))
        student_code=int(input("Enter your student code: "))
        for i in books:
            if student_code in books[i]:
                print("Book is available in shelf",i)
                book_returned=books[i].remove(student_code)
                print("Book returned successfully")
                books[i].append(book)
                print(f"The book {book} has been returned by the student {student_code} ")
                break
            else:
                print("Book is not available")
    elif ans==5:
        print("Thank you for using the library")
        break
    else:
        print("Invalid input")
        continue
