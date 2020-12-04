from Sukhdev_Dhaba import *
from Koyal import *
from Mannat_Haveli import *
from Payment import *

class Multiple_Order_Selection(Sukhdev_dhaba,Koyal,Mannat_Haveli):

    def multiple_order(self,restau_S,restau_K,restau_M):

        self.multiple_order_list = {}
        self.max_order = 3 
        
        print("!!! Restaurants available now are ----\n")
        
        print("1.SUkhdev Dhaba \n2.Koyal \n3.Mannat Haveli\n")
        
        self.res_name = input("Choose the restaurant by number: \n")
        n = 1
        if self.res_name == '1':#SUkhdev Dhaba
            
            for key in restau_S.menu_sukhdev:
                print(n,". ",key,':',restau_S.menu_sukhdev[key])
                n = n + 1
            for i in range (self.max_order):
                self.choice = input("Enter the name of the item  you want to order: ").lower()
                print()
                self.multiple_order_list[self.choice]=restau_S.menu_sukhdev[self.choice]
                                    
                if i == 1:
                    self.choice = input("Do you wish to add more food from Sukhdev Dhabha . Press Y  for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("Your Cart is almost full!! This is the last item you can order")
                        print()
                        self.choice = input("Enter your last item name  which you wish to add: ").lower()
                        print()
                        self.multiple_order_list[self.choice]=restau_S.menu_sukhdev[self.choice]
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
                Payment.order_payment(self.multiple_order_list)
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return


        elif self.res_name == '2':#Koyal

            for key in restau_K.menu_koyal:
                print(n,key,':',restau_K.menu_koyal[key])
                n = n + 1
            for i in range (self.max_order):
                self.choice = input("Enter the item name you wish to order: ").lower()
                print()
                self.multiple_order_list[self.choice]=restau_K.menu_koyal[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food From Koyal Restaurant. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("Your Cart is almost full!! This is the last item you can order")
                        print()
                        self.choice = input("Enter your last item name  which you wish to add: ").lower()
                        print()
                        self.multiple_order_list[self.choice]=restau_K.menu_koyal[self.choice]
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
                Payment.order_payment(self.multiple_order_list)
               

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

        elif self.res_name == '3':#Mannat Haveli

            for key in restau_M.menu_mannat:
                print(n,key,':',restau_M.menu_mannat[key])
                n = n + 1
            max_order = 3 
            for i in range (max_order):
                self.choice = input("Enter the item name you wish to order: ").lower()
                print()
                self.multiple_order_list[self.choice]=restau_M.menu_mannat[self.choice]
                if i == 1:
                    self.choice = input("Do you wish to add more food from Mannat. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print("Your Cart is almost full!! This is the last item you can order")
                        print()
                        self.choice = input("Enter your last item name  which you wish to add: ").lower()
                        print()
                        self.multiple_order_list[self.choice]=restau_M.menu_mannat[self.choice]
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
                Payment.order_payment(self.multiple_order_list)

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return