
from itertools import product


class Checkout:
    '''
    class for checkout
    '''

    def __init__(self,customer:str):
        '''
        init for an order
        '''
        try:
            customer.lower()
        except:
            print("please enter a vaild name")

        self.customer = customer.lower() #switch everything to lower case
        self.item = []
        self.product = ["small pizza","medium pizza","large pizza"]
        
        #price for different pizza
        self.sPizza = 11.99
        self.mPizza = 15.99
        self.lPizza = 21.99

    def add(self,itemName:str):
        '''
        add item
        '''
        try:
            itemName.lower()
        except:
            print("please enter a vaild name")
            return

        if itemName.lower() in self.product:
            self.item.append(itemName.lower())
        else:
            print("No such type of pizza")
            # raise NameError("No such type of pizza")

    def total(self):
        '''
        calculate total
        '''
        total = 0
        s,m,l = 0,0,0
        for i in self.item:
            if i == "small pizza":
                s += 1
            elif i == "medium pizza":
                m += 1
            elif i == "large pizza":
                l += 1
            else:
                pass


        if self.customer == "microsoft":
            total = s//3 * (self.sPizza * 2) + s%3 * self.sPizza + m * self.mPizza + l * self.lPizza       #pricing rule for microsoft (small pizza 3 for 2)
        elif self.customer == "amazon":
            total = s * self.sPizza + m * self.mPizza + l * 19.99       #special price for large pizza #prcing rule for amazon (large pizza 19.99)
        elif self.customer == "facebook":
            total = s * self.sPizza + m//5 * (self.mPizza * 4) +  m%5 * self.mPizza + l * self.lPizza        #pricing rule for facebook (medium pizza 4 for 5)
        else:
            total =  s * self.sPizza + m * self.mPizza + l * self.lPizza  #no discount

        print("Total $",total)
        return total
    

