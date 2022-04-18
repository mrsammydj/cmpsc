#Cashier/inventory management system



class Inventory:
    '''Create inventory class'''
    def __init__(self, inv):
        self.inv = inv


    def addInv(self):
        new_item_name = input("Please input the name for a new item: ").capitalize()
        new_item_barcode = input("Please input a barcode for this new item: ")
        new_item_price = input("Please input a price for this new item: ")
        self.inv[new_item_barcode] = new_item_name, new_item_price
        print()
        print("Item [",new_item_name,"] has been added to the inventory!",sep="")
        print()
        return self


    def delInv(self):
        removed_barcode = int(input("Please input a barcode to delete: "))
        for key in self.inv:
            if removed_barcode == key:
                print("Item [",self.inv[key][0],"] has been deleted to the inventory!",sep="")
                del self.inv[key]
                break
            

    def editInv(self):
        edited_barcode = int(input("Please input a barcode to edit: "))
        for key in self.inv:
            if edited_barcode == key:
                self.inv[key][0] = (input("Please input a name for this item: ")).capitalize()
                self.inv[key][1] = input("Please input a price for this item: ")
                print("Item successfully edited!")
                break


    def displayInv(self):
        print()
        print("{: >20} {: >20} {: >20}".format("Item Name", "Barcode", "Price"))
        print()
        for key in self.inv:
            print("{: >20} {: >20} {: >20}".format(self.inv[key][0], key, ("$"+str(self.inv[key][1]))))
        print()
        

class Cart(Inventory):
    '''Customer shopping cart class'''
    def __init__(self, cart, inv):
        self.cart = cart
        self.inv = super().__init__(inv)
        print(vars(inv))

    
    def scanning(self, inv):
        Inventory.displayInv(inv)
        print(isinstance(inv, Inventory))
        scanned = 0
        while scanned != "pay":
            scanned = input("Input a barcode to scan or type 'pay' to pay: ")
            if scanned.isdigit():
                scanned = int(scanned)
            for key in self.inv:
                if key == scanned:
                    print(self.inv[key])
                    Cart.updateCart(self.cart, self.inv, key)
                    total_price, total_items = Cart.updateTotals(self)
                    Cart.displayCart(self, total_items, total_price)
                    break
        print()
        print("Thank you for shopping!")
    

    def updateCart(self, inv, key):
        self[key] = inv[key]
        print(self)


    def updateTotals(self):
        total_price = 0
        total_items = 0
        for key in self.cart:
            total_price += int(self.cart[key][1])
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

    inv.addInv()
    shoppingcart.scanning(inv)
    

main()

