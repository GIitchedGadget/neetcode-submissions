class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for i in range(len(nums)):
            if i == 0:
                result.append(1)
            else:
                product *= nums[i - 1]
                result.append(product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= product
            product *= nums[i]
            
        print(result)
        return result
        