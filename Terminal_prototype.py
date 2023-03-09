'''
This app calculates how much each person owe each other
'''

print("Hello, and welcome to the app. Please add how many users will be using this app")
number_of_users = input("Type a number: ")
users = []
i = int(number_of_users)
x = 1
while i > 0:
    users.append(input("Please add user " + str(x)+ ": "))
    i = i -1
    x = x + 1

print(users)

transactions = [[],[],[]]

print("What would you like to do? Type the number: 1 to add another user, 2 to add a transaction, 3 to calculate current transaction")#this will be the UI
option = int(input("Type now: "))

if option == 1:
    add_user()#database

if option == 2:
    add_transaction()#database

if option == 3:
    calculate()#algorithm 

add_transaction()

def add_transaction():
    transactions.insert(0,input("Give the transaction a name: "))
