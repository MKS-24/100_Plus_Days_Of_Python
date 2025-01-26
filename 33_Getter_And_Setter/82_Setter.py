class myclass:
    def __init__(self,price):
        self.price = price
    def printprice(self):
        print("Price is : ", self.price)

    @property
    def whatprice(self):
        return self.price 
    @whatprice.setter
    def whatprice(self,new):  # name same ona lzzmi nh hai function ka
        self.price = new
    
obj = myclass(10)
obj.printprice()
print(obj.whatprice)
obj.whatprice = 50
obj.printprice()


                