def printInventory(inventory):
    for i in range(len(inventory)):
        print("{pos}. {item}".format(pos=i + 1, item=inventory[i]))


inventory = [
    "Coke",
    "Pepsi",
    "Fanta",
    "Dew",
    "Juice",
    "Mango",
    "Banana",
    "Juice",
    "Mango",
    "Banana",
]

inventory.append("new product")
printInventory(inventory)
inventory.append("new product 2")

printInventory(inventory)
