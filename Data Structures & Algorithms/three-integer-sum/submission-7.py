class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        results = []
        for i in range(0, length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            p1 = i + 1
            p2 = length - 1
            while p1 < p2:

                sum = nums[p1] + nums[p2]
                if sum == target:
                    results.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1 - 1] == nums[p1]:
                        p1 += 1
                    while p1 < p2 and nums[p2 + 1] == nums[p2]:
                        p2 -= 1
                    continue
                elif sum > target:
                    p2 -= 1
                    continue
                else:
                    p1 += 1
        return results        
                


        