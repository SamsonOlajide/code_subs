class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num_len = len(nums)
        for i in range(num_len-1):
            if nums[i] == nums[i+1]:
                return True
                break
        return False