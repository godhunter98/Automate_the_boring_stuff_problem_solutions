from Chapter05_Fantasy_Game_Inventory import displayInvetory
# we're importing the function we created in last exercise

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def addToInventory(inventory:dict,addedItems:list):
    for item in addedItems:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1
    return inventory

new_inv = addToInventory(inv,dragonLoot)
displayInvetory(new_inv)