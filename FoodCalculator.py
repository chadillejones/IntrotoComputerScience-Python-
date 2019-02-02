# FoodCalculator.py
# This class allows users to add the prices of food items one at a time, and to calculate the tax, tip, and total cost for the added food items.

# The class should be named FoodCalculator.
# The __init__ method should take no arguments.
# There should be an add_item method that takes a float and adds it to the current price.
# There should be a get_tax method that takes a float representing the tax rate and returns the tax on the current price.
# There should be a get_tip method that takes a float representing the tax and a float representing the tip, and returns the cost of the tip on the current price, assuming tip is calculated after tax.
# There should be a method called get_total_cost that takes in a float representing the tax, and a float representing the tip, and returns the total cost of the meal based on the current cost, tax, and tip.

# Example Code: (This code should work, and give the expected results, if your code is correct.

class FoodCalculator():
    
    def __init__(self):
        self.price=0.0
        self.tax=0.0
        self.tip=0.0
        self.total=0.0
        
    def add_item(self, num):
        self.price+=num
        
    def get_tax(self, tax):
        tax_rate=tax/100
        self.tax=self.price*tax_rate
        print(self.tax)
        return(self.tax)
        
    def get_tip(self, tax, tip):
        tax_rate=tax/100
        self.tax=self.price*tax_rate
        self.total=self.tax+self.price
        tip_rate=tip/100
        self.tip=self.total*tip_rate
        print(self.tip)
        return(self.tip)
        
    def get_total_cost(self, tax, tip):
        tax_rate=tax/100
        self.tax=self.price*tax_rate
        self.total=self.tax+self.price
        tip_rate=tip/100
        self.tip=self.total*tip_rate
        gtotal=self.total+self.tip
        print(float(gtotal))
        return(float(gtotal))

foodcalc = FoodCalculator()
foodcalc.add_item(100.00)
foodcalc.add_item(1900.00)
foodcalc.get_tax(10) # 200.0
foodcalc.get_tip(10, 20) # 440.0
foodcalc.get_total_cost(10, 20) # 2640.0
