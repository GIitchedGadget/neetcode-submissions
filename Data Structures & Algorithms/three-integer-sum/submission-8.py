class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for i in range(0, length):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p1 = i + 1
            p2 = length - 1
            target = nums[i] * -1
            while (p1 < p2):

                if nums[p1] + nums[p2] == target:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while nums[p1] == nums[p1 - 1] and p1 < length - 1:
                        p1 += 1
                    while nums[p2] == nums[p2 + 1] and p2 > 0:
                        p2 -= 1

                elif nums[p1] + nums[p2] > target:
                    p2 -= 1
                else:
                    p1 += 1

        return result
                    

        