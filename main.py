from single_order import *
from multiple_order import * 
from Sukhdev_Dhaba import *
from Koyal import *
from Mannat_Haveli import *
from update_menu import *



singl = Single_Order_Selection()
multple = Multiple_Order_Selection()
updation = Update_Menu()
restau_S = Sukhdev_dhaba()
restau_K = Koyal()
restau_M = Mannat_Haveli() 
restau_S.food_item()
restau_K.food_item()
restau_M.food_item()

print("\n", "~ " * 7 + "      WELCOME TO Swiggy!!!     "+ "~ " * 7,"\n")
print("  Choose your options here :- \n")
print(" 1 For Food ordering ")
print(" 2 To QUIT \n")
choice = input(">> Enter your option : ")
print()
if choice == '1':
    print(">> You are:-  \n\n 1.CUSTOMER \n 2.Restaurant OWNER \n")
    choice = input(" Enter your option : \n")
    if choice == '1':
            
        print(" 1 For single order with lowest price \n 2 to  Select through restaurants and order multiple items \n")
        choice = input(">> Enter your Choice :")
        print()
        if choice == '1':
            singl.single_order(restau_S, restau_K,restau_M)
            
        elif choice == '2':
            multple.multiple_order(restau_S, restau_K, restau_M)
                    
    elif choice == '2':
        while True:
            print("Enter the your password")
            password = input()
            if password == 'owner':
                updation.add_item(restau_S, restau_K, restau_M)
            else:
                print("Invalid password")
            break

        
else :
    print("~" * 5 +"   Goodbye :\ Enjoy your day     " + "~" * 5 ,"\n")