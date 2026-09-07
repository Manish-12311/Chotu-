
bal=10000
withdrawal=True

while withdrawal:
    amount=int(input("enter the amount: "))
    if amount<=bal:
        print("amount debited ")
        bal=bal-amount
        print("your current balance :",bal)
    else:
        print("insufficient bal")
        
    choice=(input("do you need to withdraw again :"))
    if choice.lower()=="yes":
        withdrawal=True
    if choice.lower()=="no":
        withdrawal=False