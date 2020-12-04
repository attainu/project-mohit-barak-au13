import time
import ast
class Payment:
    def order_payment(order):#a list which is dictionary where all food items and price is stored.
        selected_items = []
        for item in order:
            selected_items.append(item)
        print(">> You have selected: \n")
        for key  in selected_items:
            print(key)
        print()
        sum = 0
        for i in order: 
            sum = sum + int(order[i])
            CGST = sum * (2.5/100)
            SGST = sum * (2.5/100)
            updated_sum = sum + CGST + SGST
        
        print(">> Your total amount of all items is ₹ : ",sum)
        print("CGST is:                                 ",CGST)
        print("SGST is:                                 ",SGST,"\n"*2)
        print("Final amount to be paid after CGST and SGST is ₹ : ",updated_sum,"\n")
        print("Please give your Contact Details")
        First_name = input("* First Name :")
        Last_name = input("* Last Name :")
        Phone_number = int(input("* Phone Number:"))
        Address = input("* Address :")
        print("Please select the payment method : \n")
        n = input(" 1.COD \n 2.UPI \n 3.Debit/Credit card \n\n--- Choose your option :")
        print("~" * 30)
        print(" Your Delivery Details Are :\n")
        print(f" First name : {First_name}")
        print(f" Last name : {Last_name}")
        print(f" Phone number : {Phone_number}")
        print(f" Delivary Address : {Address}")
        print("~" * 30)
        time.sleep(3)
        print()
        
        if n == '1':
            print("Request has been accepted and you choose for Cash on delivery....\n")
            
        elif n == '2':
            n = input(" Please enter your UPI ID: ")
            print()
            m = input(" Enter pin :")
            print("Your payment is in progress.....\n")
            time.sleep(3)
            print("Payment has been accepted.....\n")
        elif n == '3':
            print(" Please enter your Card Details: \n")
            m = int(input(">> Enter Card Number :"))
            z = int(input(">> Enter CVV :"))
            time.sleep(3)
            y = input(">> Enter OTP :")
            print("Your payment is in progress.....\n")
            time.sleep(3)
            print("Payment has been accepted....\n")
        print()       
           

        print("We are preparing your food......\n")
        time.sleep(5)

        print("~" * 8 +"   Your food is ready and out for  delivery. It will reach by you in 20 minutes    " + "~" * 8,"\n")

        print("~" * 20 +"   ENjoy Your Meal   "+ "~" * 20,"\n")
        

