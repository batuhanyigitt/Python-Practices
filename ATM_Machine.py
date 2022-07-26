print("""***********************************

Welcome to the ATM Machine.

Transactions;

1.Balance Inquiry

2.Deposit

3.Withdraw money

Please press 'q' to exit the ATM.

*****************************************
""")

balance= 1000

while True:
    process = input("Select the transaction:")

    if (process== "q"):
        print("we are waiting for you again")
        break
    elif (process  == "1"):
       print("Your balance {} tl dir".format(balance))


    elif (process == "2"):
        quantity = int(input("Enter amount:"))
        balance += quantity 

    elif (process == "3"):
        quantity = int(input("Enter amount:"))

        if (balance - quantity < 0):
            print("You cannot withdraw such an amount...")
            continue
        balance -= quantity

    else:
        print("Invalid operation....")