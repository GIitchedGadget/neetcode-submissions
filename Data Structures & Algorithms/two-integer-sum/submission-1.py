class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            lookFor = target - nums[i]
            ptr = i + 1
            while ptr < length:
                print(ptr)
                if nums[ptr] == lookFor:
                    return [i, ptr]
                ptr += 1
                
                
        