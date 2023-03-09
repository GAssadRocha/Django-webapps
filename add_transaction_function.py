transactions = [[],[],[],[]]

def add_transaction():
    transactions[0] = input("Give the transaction a name: ")

    transactions[1] = input("Who paid? ")

    number_owes = int(input("How many people it was paid to? "))
    i = 0
    while i < number_owes:
        transactions[2].append(input("Person " + str(i + 1) + ": "))
        i = i + 1
    
    transactions[3] = int(input("Total amount: "))

    

add_transaction()

print(transactions)
print(transactions[0])
print(transactions[1])