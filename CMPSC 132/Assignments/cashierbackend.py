#Cashier/inventory management system

import unittest


class Inventory:
    '''Create inventory class'''
    def __init__(self, inv):
        self.inv = inv


    def addItem(self, code, item_name, item_price):
        self.inv[code] = item_name, item_price
        print()
        print("Item [",item_name,"] has been added to the inventory!",sep="")
        self.displayItemDetails(code)


    def delItem(self, code):
        self.displayInv()
        print("Item [",self.inv[code][0],"] has been deleted to the inventory!",sep="")
        del self.inv[code]
            

    def editItem(self, code, item_name, item_price):
        self.displayInv()
        self.inv[code][0] = item_name
        self.inv[code][1] = item_price
        print("Item [",self.inv[code][0],"] has been successfully edited!", sep="")
    
    def retrieveItemSet(self, code):
        for key in self.inv:
                if key == code:
                    return self.inv[key]

    def retrieveItemPrice(self, code):
        for key in self.inv:
                if key == code:
                    return self.inv[key][1]
    


    def displayInv(self):
        print()
        print("{: >20} {: >20} {: >20}".format("Item Name", "Barcode", "Price"))
        print()
        for key in self.inv:
            print("{: >20} {: >20} {: >20}".format(self.inv[key][0], key, ("$"+str(self.inv[key][1]))))
        print()
        
    def displayItemDetails(self, key):
        print()
        print("Item name:", self.inv[key][0])
        print("Barcode:",key)
        print("Price: $", self.inv[key][1],sep="")
        print()



class Cart(Inventory):
    '''Customer shopping cart class'''
    def __init__(self, cart, inv):
        self.cart = cart
        super().__init__(inv)

    
    def scanning(self):
        Inventory.displayInv(self.inv)
        scanned = 0
        while scanned != "pay":
            scanned = input("Input a barcode to scan or type 'pay' to pay: ")
            if scanned.isdigit():
                scanned = int(scanned)
                scanned = Inventory.retrieveItemSet(self.inv, scanned)
                self.updateCart(scanned)
                total_price, total_items = self.updateTotals(self.inv)
                Cart.displayCart(self, total_items, total_price)
                break
        print()
        print("Thank you for shopping!")
    

    def updateCart(self, key):
        self.cart[key] = Inventory.retrieveItemSet(self.inv, key)



    def updateTotals(self, inv):
        total_price = 0
        total_items = 0
        for key in self.cart:
            price = Inventory.retrieveItemPrice(self.inv, key)
            total_price += price
            total_items += 1
        return total_price, total_items

    
    def displayCart(self, total_items, total_price):
        print()
        print("{: >36}".format("---Your Cart---"))
        print()
        print("{: >20} {: >20} ".format("Item", "Price"))
        print()
        for key in self.cart:
            print("{: >20} {: >20}".format(self.cart[key][0], ("$"+str(self.inv[key][1]))))
        print("------------------------------------------")
        print("Total price: {: >28}".format("$"+str(total_price)))
        print()
        

    class TestInv(unittest.TestCase):
        '''Unit testing'''
        def test_addItem(self):
            pass

        def test_delItem(self):
            pass

        def test_editItem(self):
            pass

        def test_addItem(self):
            pass

        def test_displayItemDetails(self):
            pass

        def test_displayInv(self):
            pass
            



            
def main():

    inv = Inventory({0:["Boots",34],
                1:["T-shirt",12],
                2:["Jeans", 25],
                3:["Socks", 4]
                }
                )

    shoppingcart = Cart({}, inv)

    unittest.main()


    

main()

