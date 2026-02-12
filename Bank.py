
amount = float(input("Enter the amount"))
x = input("Enter your choice -> deposit, withdraw , balance")
def deposit(balance):
    credit=float(input("Enter the amount you are depositing"))
    return amount+credit
def withdraw():
    debit=float(input("Enter the amount you are depositing"))
    return amount-debit
def balance():
    return amount


bank = {"deposit": deposit, 
        "withdraw": withdraw,
       "balance": balance}

print(bank[x]())