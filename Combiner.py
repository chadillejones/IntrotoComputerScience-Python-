# Combiner.py:
# This class takes two arrays of integers in when created, and can calculate either all possible sums or all possible multiplications consisting of one item from each array.

# The class should be named Combiner
# The __init__ method should take two int arrays as arguments.
# There should be a combine_addition method that takes no parameters and returns a list of the results of all additions consisting of one item in the first list, and one item in the second list.
# There should be a combine_addition method that takes no parameters and returns a list of the results of all multiplications consisting of one item in the first list, and one item in the second list.
# Order does not matter for the returned results.

# Example Code: (This code should work, and give the expected results, if your code is corrclass
class Combiner():
    
    def __init__(self,arry,arry2):
        self.arry=arry
        self.arry2=arry2
        self.add=[]
        self.mult=[]
        
    def combine_addition(self):
        for x in range(0,len(self.arry)):
            for y in range(0,len(self.arry2)):
                int_pholder=self.arry[x]+self.arry2[y]
                self.add.append(int_pholder)
        print(self.add)
        return(self.add)
        
    def combine_multiplication(self):
        for x in range(0,len(self.arry)):
            for y in range(0,len(self.arry2)):
                int_pholder=self.arry[x]*self.arry2[y]
                self.mult.append(int_pholder)
        print(self.mult)
        return(self.mult)
    
combiner = Combiner([1, 2], [0, 1])
combiner.combine_addition() # [1, 2, 2, 3]
combiner.combine_multiplication() # [0, 1, 0, 2]


