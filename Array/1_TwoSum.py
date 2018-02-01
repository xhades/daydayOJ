# !/usr/bin/env python
# -*-coding:utf-8-*-

"""
@author: xhades
@Date: 2018/1/3

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, num in enumerate(nums):
            if target-num in map:
                return map[target-num], i
            map[num]=i



if __name__ == "__main__":
    x = Solution().twoSum([3, 3, 4, 9], 6)
    print(x)