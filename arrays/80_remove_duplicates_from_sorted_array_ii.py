from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for x in nums:
            if write < 2 or x != nums[write - 2]:
                nums[write] = x
                write += 1
        return write
                