class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] 
        matching_bracket = {')': '(', '}': '{', ']': '['} 
        for x in s: 
            if x in matching_bracket.values(): 
                stack.append(x) 
            elif x in matching_bracket.keys(): 
                if stack == [] or matching_bracket[x] != stack.pop(): 
                    return False 
                    
            else: 
                continue 
        return stack ==[]