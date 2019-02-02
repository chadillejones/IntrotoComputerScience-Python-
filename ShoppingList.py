# ShoppingList.py
# This class lets the user add and remove items from a virtual cart, keeping track of both the items and their prices, and being able to tell the user the total cost of all the items in their cart.

# The class should be named ShoppingList.
# The __init__ method should take no arguments.
# There should be an add_item method that takes a string representing the item name and an integer representing its price, and keeps track of that item.
# There should be a remove_item method that takes a string representing an item name, and removes the item with that name from the card. (You may assume names will be unique within a cart.)
# There should be a get_total method that returns the sum of the costs of all the items in the cart.

# Example Code: (This code should work, and give the expected results, if your code is correct.

class ShoppingList():
     
    def __init__(self):
        self.items={}
         
    def add_item(self, name, price):
        self.items.update( {name:price} )
        
        
    def remove_item(self, name):
        del self.items[name]
        
    def get_total(self):
        return(sum(self.items.values()))

shoppinglist = ShoppingList()
shoppinglist.add_item("water", 1.25)
shoppinglist.add_item("milk", 4.35)
shoppinglist.add_item("orange juice", 5.00)
shoppinglist.get_total() # 10.6
shoppinglist.remove_item("orange juice")
shoppinglist.get_total() # 5.6
