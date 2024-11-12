class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newNums = []
        for i in nums:
            j = i * i
            newNums.append(j)
            
        newNums.sort()
        return newNums
