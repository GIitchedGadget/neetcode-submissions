class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        noZeroProduct = 1
        firstZero = True
        for i in nums:
            product *= i
            if i == 0:
                if firstZero:
                    firstZero = False
                else:
                    noZeroProduct = 0
            else:
                noZeroProduct *= i

        for i in range(0, len(nums)):

            if nums[i] == 0:
                nums[i] = noZeroProduct
            else:
                nums[i] = int(product / nums[i])

        return nums

        
        