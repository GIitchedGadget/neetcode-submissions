class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        product2 = 1
        zeroFound = False
        for i in nums:
            product *= i
            if i != 0:
                product2 *= i
            else:
                if zeroFound == False:
                    zeroFound = True
                    continue
                else:
                    product2 *= i

        print(product)
        print(product2)
        
        for i in nums:
            if i != 0:
                result.append(int(product / i))
            else:
                result.append(product2)
        
        return result

        