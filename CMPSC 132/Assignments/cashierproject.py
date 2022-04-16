#Cashier/inventory management system



class Inventory:
    '''Create inventory class'''
    def __init__(self, inv):
        self.inv = inv


class addInv(Inventory):
    '''Add to inventory class'''
    def __init__(self):
        Inventory.__init__(self) 
    
    def add(self):
        new_item_name = input("Please input the name for a new item: ")
        new_item_barcode = input("Please input a barcode for this new item: ")
        new_item_price = input("Please input a price for this new item: ")
        self.inv[new_item_barcode] = [new_item_name, new_item_price]


class delInv(Inventory):
    '''Remove from inventory class'''
    def __init__(self):
        Inventory.__init__(self) 

    def delete(self):
        displayInv.__str__(self)
        removed_barcode = int(input("Please input a barcode to delete: "))
        for key in self.inv:
            if removed_barcode == key and self.inv[key][0][-1] == "s":
                print(self.inv[key][0],"have been deleted from the inventory!")
                del self.inv[key]
                break
            if removed_barcode == key and self.inv[key][0][-1] != "s":
                print(self.inv[key][0],"has been deleted from the inventory!")
                del self.inv[key]
                break
        

class editInv(Inventory):
    '''Edit inventory class'''
    def __init__(self):
        Inventory.__init__(self) 

    def edit(self):
        displayInv.__str__(self)
        edited_barcode = int(input("Please input a barcode to edit: "))
        for key in self.inv:
            if edited_barcode == key:
                self.inv[key][0] = (input("Please input a name for this item: ")).capitalize()
                self.inv[key][1] = input("Please input a price for this item: ")
                print("Item successfully edited!")
                break


class displayInv(Inventory):
    '''Display inventory class'''
    def __init__(self):
        Inventory.__init__(self) 
    
    def __str__(self):
        print()
        print("{: >20} {: >20} {: >20}".format("Item Name", "Barcode", "Price"))
        print()
        for key in self.inv:
            print("{: >20} {: >20} {: >20}".format(self.inv[key][0], key, ("$"+str(self.inv[key][1]))))
        print()
        

class Cart(Inventory):
    '''Customer shopping cart class'''
    def __init__(self, cart):
        Inventory.__init__(self)
        self.cart = cart


def main():

    inventory = {0:["Boots",34],
                1:["T-shirt",12],
                2:["Jeans", 25],
                3:["Socks", 4]
                }


    inv = Inventory(inventory)


    editInv.edit(inv)




main()

