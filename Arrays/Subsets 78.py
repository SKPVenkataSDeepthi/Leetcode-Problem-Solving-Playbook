'''''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,035,517/3.7M
Acceptance Rate
82.3% '''''

class Solution(object):
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            res += [curr + [num] for curr in res]

        return res
