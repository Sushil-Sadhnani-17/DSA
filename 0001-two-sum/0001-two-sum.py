class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}

        for i in range(n):
            nums_dict[nums[i]] = i
        
        for i in range(n):
            comp = target - nums[i]
            if comp in nums_dict and nums_dict[comp] != i:
                return [i, nums_dict[comp]]