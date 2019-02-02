# Math.py:
# This class lets us start with a number, and then do a series of mathematical operations to it, and then get our result.

# The class should be named Math
# The __init__ method should take an integer as an argument.
# There should be an add method that takes an integer and adds that to the current result.
# There should be a multiply method that takes an integer and multiplies the current result by that.
# There should be a subtract method that takes an integer and subtracts that from the current result.
# There should be a divide method that takes an integer and divides the current result by that.
# There should be a get_result method that takes no arguments and returns the current result.

# Example Code: (This code should work, and give the expected results, if your code is correct.
class Math():
    
    def __init__(self,num):
        self.result=num
        
    def add(self,num):
        self.result+=num
    
    def multiply(self,num):
        self.result*=num
        
    def subtract(self,num):
        self.result-=num
        
    def divide(self,num):
        self.result//=num
        
    def get_result(self):
        print(self.result)
        return self.result
        

math = Math(10)
math.add(5)
math.multiply(2)
math.get_result() # 30
math.subtract(10)
math.divide(5)
math.get_result() # 4
