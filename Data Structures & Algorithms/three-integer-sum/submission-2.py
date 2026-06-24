class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):

            #handle duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1

            #two sums
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                s = nums[p1] + nums[p2]
                if s > target:
                    p2 -= 1
                elif s < target:
                    p1 += 1
                else:
                    results.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1


        return results