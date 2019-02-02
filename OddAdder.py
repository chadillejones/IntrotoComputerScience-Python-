# OddAdder.py:
# This class will let people add items one at a time, or as an array, and will keep track of all of the odd items added to it, as well as telling people what the total sum of all the things its keeping track of is.

# This class should be named OddAdder.
# The __init__ method should take no arguments.
# There should be an add_item method that takes in an integer and keeps track of it if it is odd, but not if it is even.
# There should be an add_items method that takes in an array of integers and keeps track of all of the ones that are odd, but not any of the even ones.
# There should be an add_all method that takes no parameters, and returns the sum of all the items the class is keeping track of.

# Example Code: (This code should work, and give the expected results, if your code is correct.
class OddAdder():
    
    def __init__(self):
        self.odd = []
        
    def add_item(self, pholder):
        if pholder % 2 == 1:
            self.odd.append(pholder)
    
    def add_items(self, pholders):
        int_x=0
        while int_x < len(pholders):
            if pholders[int_x] % 2 == 1:
                int_num=pholders[int_x]
                self.odd.append(int_num)
            int_x+=1
                
    def add_all(self):
        int_odd_total=sum(self.odd)
        print(str(int_odd_total))
        return(int_odd_total)
        

oddadder = OddAdder()
oddadder.add_items([3, 3, 4, 1])
oddadder.add_all() # 7
oddadder.add_item(4)
oddadder.add_all() # 7


