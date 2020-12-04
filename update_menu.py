from Sukhdev_Dhaba import *
from Mannat_Haveli import *
from Koyal import *


class Update_Menu(Sukhdev_dhaba,Koyal,Mannat_Haveli):

    def add_item(self,restau_S, restau_K, restau_M):

        print("!!! We have restaurants....\n")
        
        print("1.Sukhdev Dhabha"," \n2.Koyal"," \n3.Mannat Haveli\n")
        self.res_name = input("Now select your restaurant by entering no.: ")
        print()
        
        if self.res_name == '1':
            print(" Your menu : ")
            for key in restau_S.menu_sukhdev:
                print(key,':',restau_S.menu_sukhdev[key])
            print("Press : \n 1 to Add any dish \n 2 to R any dish \n 3 to EXIT \n")
            self.op = input("Choice :")
            print()
            if self.op == '1':
                print("your menu: ")
                for key in restau_S.menu_sukhdev:
                    print(key,':',restau_S.menu_sukhdev[key])
                self.item = input("Add the name of dish: ")
                self.price = input("Add the price: ")
                print()
                restau_S.menu_sukhdev[self.item]=self.price
                print("Your new menu is: ")
                for key in restau_S.menu_sukhdev:
                    print(key,':',restau_S.menu_sukhdev[key])
                print("Now load the app again we are exiting you from the app")

            elif self.op == '2':
                for key in restau_S.menu_sukhdev:
                    print(key,':',restau_S.menu_sukhdev[key])
                self.item = input("Enter the dish name you want to remove: ")
                print()
                del restau_S.menu_sukhdev[self.item]
                print("Your new menu is: ")
                for key in restau_S.menu_sukhdev:
                    print(key,':',restau_S.menu_sukhdev[key])
                print("Now load the app again we are exiting you from the app")
            
            elif self.op == '3':
                return

        elif self.res_name == '2':
            print(">> Your menu : ")
            for key in restau_K.menu_koyal:
                print(key,':',restau_K.menu_koyal[key],"\n")
            print(">> Press : \n\n1 to Add dish \n2 to Remove dish \n3 to EXIT \n")
            self.op = input(">> Choice :")
            print()
            if self.op == '1':
                print("Dishes in your menu :")
                for key in res_B.menu_S:
                    print(key,':',res_B.menu_S[key])
                
                self.item = input("Enter the name of dish: ")
                self.price = input("Add the price: ")
                print()
                res_B.menu_S[self.item]=self.price
                print("Your new menu is: ")
                for key in restau_K.menu_koyal:
                    print(key,':',restau_K.menu_koyal[key])
                print("Now load the app again we are exiting you from the app")
                
                
            elif self.op == '2':
                for key in restau_K.menu_koyal:
                    print(key,':',restau_K.menu_koyal[key])
                self.item = input("Type the item you want to remove: ")
                print()
                del restau_K.menu_koyal[self.item]
                print("Your new menu is: ")
                for key in restau_K.menu_koyal:
                    print(key,':',res_B.menu_S[key])
                print("Now load the app again we are exiting you from the app")
                
            
            elif self.op == '3':
                return
                        
                    

        elif self.res_name == '3':
            for key in restau_M.menu_mannat:
                print(key,':',restau_M.menu_mannat[key])
            
            print("Press: \n1 to Add dish \n2 to Remove dish \n3 to EXIT ")
            self.op = input("Choice :")
            print()
            if self.op == '1':
                print("Your menu is : ")
                for key in restau_M.menu_mannat:
                    print(key,':',restau_M.menu_mannat[key])
                
                self.item = input("Enter the name of dish you want to add: ")
                self.price = input("Enter the price: ")
                print()
                restau_M.menu_mannat[self.item]=self.price
                print("Your new menu is: ")
                for key in restau_M.menu_mannat:
                    print(key,':',restau_M.menu_mannat[key])
                print("Now load the app again we are exiting you from the app")
                

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del restau_M.menu_mannat[self.item]
                print("Your new menu is: ")
                for key in restau_M.menu_mannat:
                    print(key,':',restau_M.menu_mannat[key])
                print("Now load the app again we are exiting you from the app")
                
            
            elif self.op == '3':
                return