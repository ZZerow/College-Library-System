#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Create a single program in Python to showcase the usage of 
# variables, operators and control statements in Python. You are free to take up any real world scenario.


# In[ ]:


### Senario : Library system for students
#RULES :
#1. When student's number of overdue overs 5, he/she can't check out books. 
#2. Overdue is Only 10days. 
#3. Only 5 books can be checked out by one person. 
#Exceptions
# 1. If the user has checked out book before, overdue date will be extended 10days from remain days. 
# 2. If the user has remaining books when trying to return book, overdueDayLeft will be same as before. 
# 3. Eventhough user bring all the overdue books, user's overdueNo will be still same. 
#Variables : 
# 1. name : Student name 
# 2. bookNo : The number of books are checked out currently
# 3. regNo : Student register number
# 4. overdueDayLeft : Left days before overdue
# 5. overdueNo : the number of books to overdue
#Operators : ==, -=, OR
#Control statements : If, For, While, Break, Continue 

end = 0 
book_db = ["Learning Python", "Fundamentals of Mathematical Statistics", "Python Crash Course"]
student_db = [{"name":"Jude", "bookNo":1, "regNo":10, "overdueDayLeft":5, "overdueNo":0}, 
              {"name":"Tom", "bookNo":5, "regNo":11, "overdueDayLeft":9, "overdueNo":10}, 
              {"name":"Marry", "bookNo":2, "regNo":12, "overdueDayLeft":0, "overdueNo":1}]


def check_rules(target) :
    rule_fail = 0 
    #Check RULE 1. 
    if target["overdueNo"] > 5 or target["overdueDayLeft"] <= 0 or target["bookNo"] > 5 : 
        print(">> Sorry, you can't check out books as you broke the rules.")
        rule_fail = 1
    return rule_fail

def print_shelves() : 
        print("=======Shelves========")
        for book in book_db : 
            print(f"[{book}]") 
        print("======================")

def print_myinfo(target) : 
        print("=======My Info========")
        print(target) 
        print("======================")    

print("Good morning! This is CHRIST Libarary! How can I help you?")
name = input(">> Hello, this is ________. Type one of those >> (Jude/Tom/Marry)")

for stu_info in student_db : #Search student from student DB based on name.
    if stu_info["name"] == name :
        target = stu_info

print_myinfo(target)
        
while end == 0 : 

    answer = int(input("Enter NUMBER : 1. Checking out 2. Returning 3. Myinfo 4. Exit"))
    
    if answer == 1 : #Checking out book 

        #Check if available books 
        if len(book_db) == 0 : 
            print(">> There's no book available.")
            continue
        #Check rules 
        if check_rules(target) : 
            continue
            
        #Book 
        print_shelves()
        book_name = input("Type the book name you want to check out.")
        
        #Remove from book db 
        if book_name in book_db : 
            book_db.remove(book_name)
            print(">> Successfully it is checked out.")
            print_shelves()
        else : 
            print(">> Sorry, there's no book has that name.")
            continue
        #Increase bookNo and renew overdue day
        target["bookNo"] += 1 
        target["overdueDayLeft"] += 10 
        
    elif answer == 2 :#Returning book 
        #Check if available to returning book 
        if target["bookNo"] <= 0 : 
            print("You don't have book to return.")
            continue
        bookRet_name = input("Type the book name to return.(Try any words)")
        #Add to db 
        book_db.append(bookRet_name)
        #bookno -1 
        target["bookNo"] -= 1 
        #If the book is overdue or not 
        if target["overdueDayLeft"] <= 0 :
            print(">> This book is overdue.")
            target["overdueNo"] += 1
        else : 
            if target["bookNo"] == 0 : # if the book was last one
                target["overdueDayLeft"] = 0 
                
        print(">> Successfully it is returned.")
        print_shelves()
        
    elif answer == 3 : #Myinfo
        print_myinfo(target)
        
    elif answer == 4 :#Exit
        print("Okay, have a good day!") 
        break
    else : 
        print("Typed wrong character. ")


