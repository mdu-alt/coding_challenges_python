from typing import List, Dict


class TwoSum:
    """
    Given an array of integers ``nums`` and an integer ``target``, return the indices of the two numbers such that they
    add up to ``target``.

    Constraints:
      * ``2 <= len(nums) <= 10e4``
      * ``-10e9 <= nums[i] <= 10e9``
      * ``-10e9 <= target <= 10e9``
      * Only one valid answer exists

    Reference: https://leetcode.com/problems/two-sum/
    """

    @staticmethod
    def find_indices(nums: List[int], target: int) -> List[int]:
        hashmap: Dict[int, int] = {}

        for i, n in enumerate(nums):
            if n in hashmap:
                return [hashmap[n], i]

            hashmap[target - n] = i

        return []
