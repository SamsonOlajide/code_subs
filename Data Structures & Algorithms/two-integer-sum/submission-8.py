class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, value in enumerate(nums):
            hashMap[value]= index

        for ind, val in enumerate(nums):
            diff = target - val
            if diff in hashMap and ind != hashMap[diff]:
                return [ind, hashMap[diff]]

