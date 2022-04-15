#Cashier/inventory management system

class Inventory:
    '''Create inventory class'''
    def __init__(self):
        self.inv = {0:["Boots",34],
                        1:["T-shirt",12],
                        2:["Jeans", 25],
                        3:["Socks", 4]
                        }


class AddInv(Inventory):
    '''Add to inventory class'''
    def __init__(self):
        Inventory.__init__(self) 
    
    def add(self):
        pass


class removeInv(Inventory):
    '''Remove from inventory class'''
    def __init__(self):
        Inventory.__init__(self) 


class editInv(Inventory):
    '''Edit inventory class'''
    def __init__(self):
        Inventory.__init__(self) 


class displayInv(Inventory):
    '''Display inventory class'''
    def __init__(self):
        Inventory.__init__(self) 
    
    def __str__(self):
        for i in self:
            print(self[i])


class Cart(Inventory):
    '''Customer shopping cart class'''
    def __init__(self, cart):
        Inventory.__init__(self)
        self.cart = cart


inv = Inventory()
isinstance(inv, dict)

#displayInv.__str__(inv)

