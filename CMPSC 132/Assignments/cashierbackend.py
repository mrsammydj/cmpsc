#Cashier/inventory management system

from operator import delitem
import unittest


class Inventory:
    '''Create inventory class'''
    def __init__(self, inv):
        self.inv = inv


    def getInv(self):
        return self.inv


    def addItem(self, code, item_name, item_price):
        self.inv[code] = [item_name, item_price]
        print()
        print("Item [",item_name,"] has been added to the inventory!",sep="")
        self.displayItemDetails(code)
        return self.inv


    def delItem(self, code):
        self.displayInv()
        print("Item [",self.inv[code][0],"] has been deleted to the inventory!",sep="")
        del self.inv[code]
        return self.inv
            

    def editItem(self, code, item_name, item_price):
        self.displayInv()
        self.inv[code][0] = item_name
        self.inv[code][1] = item_price
        print("Item [",self.inv[code][0],"] has been successfully edited!", sep="")
        return self.inv
    

    def retrieveItemPrice(self, code):
        for key in self.inv:
                if key == code:
                    return self.inv[key][1]
    

    def displayInv(self):
        print()
        print("{: >45}".format("---Inventory---"))
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

    
    def scanning(self, code):
        Inventory.displayInv(self.inv)
        while code != "pay":
            code = int(code)
            self.cart[code] = Inventory.getInv(self.inv)[code]
            total_price, total_items = self.updateTotals(self.inv)
            self.displayCart(total_items, total_price)
            return self.cart
        print()
        print("Thank you for shopping!")
    

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
        for code in self.cart:
            print("{: >20} {: >20}".format(self.cart[code][0], ("$"+str(self.cart[code][1]))))
        print("------------------------------------------")
        print("Total price: {: >28}".format("$"+str(total_price)))
        print()
        


class TestInv(unittest.TestCase):
    '''Unit testing'''

    def testAddItem(self):
        '''Adding item to inv unit test'''
        test_inv = Inventory({})
        print(type(test_inv))
        self.assertDictEqual(test_inv.addItem(4, "Shorts", 10), {4:["Shorts", 10]})

    def testDelItem(self):
        '''Deletiing item from inv unit test'''
        test_inv = Inventory({0:["Boots",34],
                            1:["T-shirt",12]})
        self.assertDictEqual(test_inv.delItem(0), {1:["T-shirt", 12]})

    def testEditItem(self):
        '''Editing item in inv unit test'''
        test_inv = Inventory({0:["Boots",34],
                            1:["T-shirt",12]})
        self.assertDictEqual(test_inv.editItem(1, "Long-sleeve shirt", 15), {0:["Boots",34], 1:["Long-sleeve shirt",15]})

    def testScanning(self):
        '''Adding item to cart unit test'''
        test_inv = Inventory({0:["Boots",34],
                            1:["T-shirt",12]})
        test_cart = Cart({}, test_inv)
        self.assertDictEqual(test_cart.scanning(1),{1:["T-shirt",12]})
    
    def testAddThenScan(self):
        '''Adding item to inv, then scanning that item unit test'''
        test_inv = Inventory({0:["Boots",34],
                            1:["T-shirt",12]})
        test_cart = Cart({}, test_inv)
        test_inv.addItem(3, "Shorts", 10)
        self.assertDictEqual(test_cart.scanning(3), {3:["Shorts",10]})
    
    def testScanUnknown(self):
        '''Scanning nonexistant item unit test'''
        test_inv = Inventory({0:["Boots",34],
                            1:["T-shirt",12]})
        test_cart = Cart({}, test_inv)
        self.assertRaises(KeyError, lambda: test_cart.scanning(2))



            
def main():

    unittest.main()


main()

