class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newNums=set()
        for x in nums:
            if x in newNums:
                return True
            newNums.add(x)
        return False

            
        