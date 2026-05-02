''''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

Hide Hint #1  
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
'''

class Solution(object):
    @staticmethod
    def reverseString(s):
        left = 0
        right = len(s) - 1
        while left < right:
            # Swap the elements
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

# Using the class method without creating an instance (static method)
s = ["h", "e", "l", "l", "o"]
print(Solution.reverseString(s))  # This should print ['o', 'l', 'l', 'e', 'h']

