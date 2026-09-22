class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                    total = nums[x] + nums[y]
                    if total == target:
                        return [x,y]
            

        