# menu ={
#     'Pizza':40,
#     'Pasta':50,
#     'Burger':60,
#     'Salad':70,
#     'Coffee':80,
    
# }

# print("Welcome to PYTHON Resturant ")
# print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

# order_total=0
# item_1=input("Enter the name of item you want to order =")
# if item_1 in menu:
#     order_total+=menu[item_1]
#     print(f"Your item {item_1} has been added to your orded")
    
# else:
#     print(f"Orderd item {item_1} is not available yet!")
    
# another_order=input("do you want to add another items?(yes/no)")
# if another_order =="yes":
#     item_2=input("Enter the name of second item =")
#     if item_2 in menu:
#         order_total+=menu[item_2]
#         print(f"Item {item_2} has been added to order")
#     else:
#         print(f"Ordered item {item_2} is not avaiable !")
        
# print(f"The total amount of items to pay is {order_total}")





menu = {   
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'coffee': 80,
    'salad': 70,
    'wings':40,
    'chiken chilli': 120,    
}

print("Welcome to PYTHON Resturant ")
print("pizza : Rs 40")
print("pasta : Rs 50")
print("burger : Rs 60")
print("coffee : RS 80")
print("salad : Rs 70")
print("wings : Rs 40")
print("chiken chilli : Rs 120")
ordered_total=0


item_1=input("Enter the name of items you want to ordered :")
if item_1 in menu:
    ordered_total+=menu[item_1]
    print(f"your items{item_1} has been added to your odered")
else:
    print(f"Odered items{item_1} is not available")
    
another_item=input("Do you want to added another items (yes\no) :")
if another_item=="yes":
    
    
    item_2=input("Enter the second items of the odered :")
if item_2 in menu:
    ordered_total+=menu[item_2]
    print(f"your items{item_2} has been added to your odered")
else:
    print(f"Odered items{item_2} is not available")
    
    
    
next_item=input("Do you want to added next items (yes\no) :")
if next_item=="yes":
    
    item_3=input("Enter the third items of the odered :")
    if item_3 in menu:
        ordered_total+=menu[item_3]
        print(f"your items{item_3} has been added to your odered")
    else:
        print(f"Odered items{item_3} is not available")
        

print(f"The total amount of the items to pay is {ordered_total}")
    

    
    
     