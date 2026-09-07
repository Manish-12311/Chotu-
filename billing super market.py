while True:
    Name=input("Enter Customer Name :")
    Mobile=input("Enter the Phone Number:")
    total=0
    
    while True:
        print("Enter the amount and Quantity :")
        amount= float(input("enter amount :"))
        quantity=float(input("Enter quantity :"))
        total+=amount*quantity
        repeat=input("do you want to add more items ? (yes/no) :")
        if repeat=="no" or repeat=="No" :
            break
        
    print("_"*40)
    print("Name :",Name)
    print("Mobile Number :",Mobile)
    print("Amount to be paid ",total)
    print("-"*40)
    print("******** Happy Shopping ********")
    
    
    repeat1=input("do you want to go to next customer (yes/no) :")
    if repeat1=="No" or repeat1=="no":
        break

        