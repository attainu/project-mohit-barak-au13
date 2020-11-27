# from food_ordering_system import *
from Sukhdev_Dhaba import *
from Koyal import *
from Mannat_Haveli import *
from Payment import *

class Single_Order_Selection(Sukhdev_dhaba, Koyal, Mannat_Haveli):
    
    def single_order(self,res_A,res_B,res_C):
        self.order_list = {}

        for key in res_A.menu_T:
            print(key,':',res_A.menu_T[key])

        for key in res_B.menu_S:
            print(key,':',res_B.menu_S[key])

        for key in res_C.menu_D:
            print(key,':',res_C.menu_D[key])

       
        self.item_name = input(">> Enter the item name you wish to order: ")
        print()
        
        if self.item_name in res_A.menu_T:
            self.price_A = res_A.menu_T[self.item_name]
        
            
            
        else:
            self.price_A = '9999'
        

        if self.item_name in res_B.menu_S:
            self.price_B = res_B.menu_S[self.item_name]
    
            
        else:
            self.price_B = '9999'


        if self.item_name in res_C.menu_D:
            self.price_C = res_C.menu_D[self.item_name]
            
            
        else:
            self.price_C = '9999'
    
    


        self.min_price = min(self.price_A,self.price_B,self.price_C)
        
        time.sleep(1)
        #here we checking that item input is in the given restaurant or not and second we check that if item is present then we check the price of that item is equal to min price or not
        if self.item_name in res_A.menu_T and self.min_price in res_A.menu_T[self.item_name]:
            print(self.item_name,"in Sukhdev Dhabha are quoted  lowest price that is Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            Payment.order_payment(self.order_list)

        if self.item_name in res_B.menu_S and self.min_price in res_B.menu_S[self.item_name]:
            print(self.item_name," in Koyal are quoted  lowest price that is Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            Payment.order_payment(self.order_list)

        if self.item_name in res_C.menu_D and self.min_price in res_C.menu_D[self.item_name]:
            print(self.item_name,"in Mannat Haveli are quoted  lowest price that is Rs",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
        
            Payment.order_payment(self.order_list)
            
        
            



        

            
