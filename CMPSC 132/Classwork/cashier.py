finalprice = 0
inventory = {11: "Apple", 22: "Pear", 33: "Orange", 44: "Banana", 55: "Strawberry", 66: "Tomato"}
prices = [2.99, 3.99, 5.99, 0.59, 4.99, 9.99]
person = input("Who are you? Input 'c' for customer or 'o' for owner: ")

if person == 'o':
    newItem = 0
    while newItem != 'exit':
        newItem = input("Input a new item to add to inventory, or type 'exit' to leave: ")
        if newItem == 'exit':
            break
        newBarcode = input("Input a new barcode: ")
        inventory[newBarcode] = str(newItem)
        print("New storage:",inventory)


#Couldn't figure out this part with dictionary
if person == 'c':
    item = int(input('Scan item bar code: '))
    while item != 'pay':
        for i in range(len(inventory)):
          if inventory[i] == int(item):
              x = i
        print(inventory[x], '${}'.format(prices[x]))
        finalprice += prices[x]
        print('The amount: ${}'.format(round(finalprice,2)))
        item = input('Scan item bar code or pay: ')
        print('Total amount: ${}'.format(round(finalprice,2)))