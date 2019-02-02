# Logic.py
# This class lets the user start out with a boolean value, apply boolean operations to it, and see the result at any point.

# The class should be named Logic.
# The __init__ method should take a boolean value, which will be the initial value.
# There should be a method called boolean_and, which takes one boolean value, then and's it with the current value.
# There should be a method called boolean_or, which takes one boolean value, then or's it with the current value.
# There should be a method called boolean_not, which not's the current value.
# There should be a get_value method, which returns the current value.

# Example Code: (This code should work, and give the expected results, if your code is correct.

class Logic():
    
    def __init__(self, boole):
        self.boole=boole 
        
    def boolean_and(self, boole):
        if self.boole and boole:
            self.boole=True
        else:
            self.boole=False
            
    def boolean_or(self, boole):
        if self.boole or boole:
            self.boole=True
        else:
            self.boole=False
            
    def boolean_not(self):
        if self.boole:
            self.boole=False
        else:
            self.boole=True
            
    def get_value(self):
        print(self.boole)
        return self.boole
    
logic = Logic(True)
logic.boolean_and(True)
logic.get_value() # True
logic.boolean_or(False)
logic.boolean_not()
logic.get_value() # False
