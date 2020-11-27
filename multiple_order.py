from Sukhdev_Dhaba import *
from Koyal import *
from Mannat_Haveli import *
from Payment import *

class Multiple_Order_Selection(Sukhdev_dhaba,Koyal,Mannat_Haveli):

    def multiple_order(self,res_A,res_B,res_C):

        self.mul_order_list = {}
        self.max_order = 3 
        
        print("!!! These Restaurants are open now !!!")
        print()
        
        print("1.SUkhdev Dhaba \n2.Koyal \n3.Mannat Haveli")
        print()
        
        self.res_name = input("Choose the restaurant by number: ")
        print()
        n = 1
        if self.res_name == '1':#SUkhdev Dhaba
            
            for key in res_A.menu_T:
                print(n,". ",key,':',res_A.menu_T[key])
                n = n + 1
            for i in range (self.max_order):
                self.choice = input("Enter the name of the item  you want to order: ")
                print()
                self.mul_order_list[self.choice]=res_A.menu_T[self.choice]
                                    
                if i == 1:
                    self.choice = input("Do you wish to add more food from Sukhdev Dhabha . Press Y  for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("Your Cart is almost full!! This is the last item you can order")
                        print()
                        self.choice = input("Enter your last item name  which you wish to add: ")
                        print()
                        self.mul_order_list[self.choice]=res_A.menu_T[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            
            self.py_choice = input("Do you wish to continue for PAYMENT.Press 'Y' for YES & 'N' for NO: ")
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return


        elif self.res_name == '2':#Koyal

            for key in res_B.menu_S:
                print(n,key,':',res_B.menu_S[key])
                n = n + 1
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                self.mul_order_list[self.choice]=res_B.menu_S[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food From Koyal Restaurant. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("Your Cart is almost full!! This is the last item you can order")
                        print()
                        self.choice = input("Enter your last item name  which you wish to add: ")
                        print()
                        self.mul_order_list[self.choice]=res_B.menu_S[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            
            self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ") 
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

        elif self.res_name == '3':#Mannat Haveli

            for key in res_C.menu_D:
                print(n,key,':',res_C.menu_D[key])
                n = n + 1
            max_order = 3 
            for i in range (max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                self.mul_order_list[self.choice]=res_C.menu_D[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food from Mannat. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("Your Cart is almost full!! This is the last item you can order")
                        print()
                        self.choice = input("Enter your last item name  which you wish to add: ")
                        print()
                        self.mul_order_list[self.choice]=res_C.menu_D[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input("Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            self.py_choice = input("Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ")
            print() 

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return
        





