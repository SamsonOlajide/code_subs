class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap={}
        for index, value in enumerate(nums):
            if value in hashMap and hashMap[value]!= index:
                return True
            hashMap[value] = index
        return False
            