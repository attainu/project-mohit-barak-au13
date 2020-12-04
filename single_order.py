# from food_ordering_system import *
from Sukhdev_Dhaba import *
from Koyal import *
from Mannat_Haveli import *
from Payment import *

class Single_Order_Selection(Sukhdev_dhaba, Koyal, Mannat_Haveli):
    
    def single_order(self,restau_S,restau_K,restau_M):
        self.order_list = {}

        for key in restau_S.menu_sukhdev:
            print(key,':',restau_S.menu_sukhdev[key])

        for key in restau_K.menu_koyal:
            print(key,':',restau_K.menu_koyal[key])

        for key in restau_M.menu_mannat:
            print(key,':',restau_M.menu_mannat[key])

       
        self.item_name = input(">> Enter the item name you wish to order: ")
        print()
        
        if self.item_name in restau_S.menu_sukhdev:
            self.price_sukhdev = restau_S.menu_sukhdev[self.item_name]
        
            
            
        else:
            self.price_sukhdev = '9999'
        

        if self.item_name in restau_K.menu_koyal:
            self.price_koyal = restau_K.menu_koyal[self.item_name]
    
            
        else:
            self.price_koyal = '9999'


        if self.item_name in restau_M.menu_mannat:
            self.price_mannat = restau_M.menu_mannat[self.item_name]
            
            
        else:
            self.price_mannat = '9999'
    
    


        self.min_price = min(self.price_sukhdev,self.price_koyal,self.price_mannat)
        
        time.sleep(1)
        #here we checking that item input is in the given restaurant or not and second we check that if item is present then we check the price of that item is equal to min price or not
        if self.item_name in restau_S.menu_sukhdev and self.min_price in restau_S.menu_sukhdev[self.item_name]:
            print(self.item_name,"in Sukhdev Dhabha lowest price of this is Rs: ",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            Payment.order_payment(self.order_list)

        if self.item_name in restau_K.menu_koyal and self.min_price in restau_K.menu_koyal[self.item_name]:
            print(self.item_name," in Koyal lowest price of this is Rs: ",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
            
            Payment.order_payment(self.order_list)

        if self.item_name in restau_M.menu_mannat and self.min_price in restau_M.menu_mannat[self.item_name]:
            print(self.item_name,"in Mannat Haveli lowest price for this is Rs: ",self.min_price)
            print()
            self.order_list[self.item_name]=self.min_price
        
            Payment.order_payment(self.order_list)
            
        
