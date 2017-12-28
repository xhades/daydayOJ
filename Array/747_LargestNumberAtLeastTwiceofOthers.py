#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        new_nums = nums.copy()
        new_nums.remove(largest)
        return nums.index(largest) if all(largest >= num*2 for num in new_nums) else -1