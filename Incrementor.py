# Incrementor.py
# This class takes in values at create time, as well as one at a time or as arrays, and has a method to increment all values.

# The class should be named Incrementor.
# The __init__ method should take an array of integers as an argument, and keep track of all of them.
# There should be an add_value method that takes in a single integer and keep track of it.
# There should be an add_values method that takes in an array of integers and keeps track of all of them.
# There should be an increment_values method that adds 1 to every item the class is currently keeping track of.
# There should be a get_values method that returns the current values the class is keeping track of.

# Example Code: (This code should work, and give the expected results, if your code is correct.

class Incrementor():
    
    def __init__(self, nums):
        self.nums=nums
        
    def add_value(self, num):
        self.nums.append(num)
        
    def add_values(self, nums):
        for x in range(0,len(nums)):
            pholder=nums[x]
            self.nums.append(pholder)
            
    def increment_values(self):
        for x in range(0,len(self.nums)):
            self.nums[x]+=1
            
    def get_values(self):
        print(self.nums)
        return(self.nums)

incrementor = Incrementor([2, 2, 8])
incrementor.add_value(7)
incrementor.increment_values()
incrementor.get_values() # [3, 3, 9, 8]
incrementor.add_values([1, 1, 10])
incrementor.increment_values()
incrementor.get_values() # [4, 4, 10, 9, 2, 2, 11]
