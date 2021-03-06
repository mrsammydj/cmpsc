#Cashier/inventory management system


class Inventory:
    '''Create inventory class'''
    def __init__(self, inv):
        self.inv = inv


    def addItem(self):
        new_item_name = input("Please input the name for a new item: ").capitalize()
        new_item_barcode = input("Please input a barcode for this new item: ")
        new_item_price = input("Please input a price for this new item: ")
        self.inv[new_item_barcode] = new_item_name, new_item_price
        print()
        print("Item [",new_item_name,"] has been added to the inventory!",sep="")
        print()
        return self


    def delItem(self):
        self.displayInv()
        removed_barcode = int(input("Please input a barcode to delete: "))
        for key in self.inv:
            if removed_barcode == key:
                print("Item [",self.inv[key][0],"] has been deleted to the inventory!",sep="")
                del self.inv[key]
                break
            

    def editItem(self):
        self.displayInv()
        edited_barcode = int(input("Please input a barcode to edit: "))
        for key in self.inv:
            if edited_barcode == key:
                self.inv[key][0] = (input("Please input a name for this item: ")).capitalize()
                self.inv[key][1] = input("Please input a price for this item: ")
                print("Item [",self.inv[key][0],"] has been successfully edited!", sep="")
                break
    
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
        

            
def main():

    inv = Inventory({0:["Boots",34],
                1:["T-shirt",12],
                2:["Jeans", 25],
                3:["Socks", 4]
                }
                )

    shoppingcart = Cart({}, inv)

    shoppingcart.scanning()

    

main()

