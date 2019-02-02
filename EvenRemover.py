# EvenRemover.py
# This class lets users add items into the class, get the items currently in the class, and remove all even items from the class.

# The class should be named EvenRemover.
# The __init__ method should take an array of integers and store them.
# There should be an add_item method that takes a single integer and stores it.
# There should be an add_items method that takes an array of integers and stores them.
# There should be a remove_evens method that removes all even numbers currently stored.
# There should be a get_items method that returns all items currently stored.

# Example Code: (This code should work, and give the expected results, if your code is correct.

class EvenRemover():
    
    def __init__(self, nums):
        self.nums=nums
        
    def add_item(self, num):
        self.nums.append(num)
        
    def add_items(self, nums):
        int_y=0
        while int_y < len(nums):
            pholder=nums[int_y]
            self.nums.append(pholder)
            int_y+=1
            
    def remove_evens(self):
        int_x=0
        while int_x < len(self.nums):
            if self.nums[int_x] % 2 == 0:
                self.nums.pop(int_x)
            int_x+=1
                
                
    def get_items(self):
        print(self.nums)
        return self.nums

evenremover = EvenRemover([10, 11, 4, -3, 0])
evenremover.get_items() # [10, 11, 4, -3, 0]
evenremover.remove_evens()
evenremover.add_item(3)
evenremover.add_items([1, 2, 3])
evenremover.get_items() # [11, -3, 3, 1, 2, 3]


