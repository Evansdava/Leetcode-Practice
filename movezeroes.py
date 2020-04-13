class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Move all 0s to the end of the array without modifying the relative order of other elements
        - Can the arary have anything other than integers?
        - Is the array sorted?
        - Do the items have to be moved, or can new ones be inserted?
        + Assuming it is only made of integers
        + Assuming it is in arbitrary order
        + Assuming new items can be made (not copied)
        
        Relatively naïve solution
        * Pop each 0 and append a 0 for each
        
        Not operation/time efficient (extra O(n-i) operations for each 0 found, where n is the number of elements and i is the index of the iteration), but doesn't take extra space
        
        More efficient:
        * Move each element other than 0 backwards, pushing 0s to the end
        
        Less space efficient (created new list), but max of 5 operations per element added, runs in O(n)
        
        For each element in the array
            if the element is not 0
                swap it with the first 0 in the array 
            otherwise, if it is 0
                Keep track of the index 
            
        """
        zero_indices = []
        swap_count = 0

        i = 0
        # While loop to easier use list indices
        while i < len(nums):
            # Add indexes of 0s to a list for later reference
            if nums[i] == 0:
                zero_indices.append(i)
            elif len(zero_indices) > 0:
                # Swap with the earliest 0 still in place
                nums[zero_indices[swap_count]] = nums[i]
                nums[i] = 0
                zero_indices.append(i)
                swap_count += 1
            i += 1
