class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        has = {}
        for i in range(0, length):
            k = target - nums[i]
            if k in has:
                return [has[k], i]
            
            has[nums[i]] = i
            

        