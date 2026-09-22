class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for x, y in enumerate(nums):
            diff = target - y
            if diff in hashMap:
                return[hashMap[diff],x]
            hashMap[y] = x
                