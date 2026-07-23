class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        numbers = set()
        longest = 1
        length = 1
        count = 1
        for i in nums:
            numbers.add(i)

        for i in numbers:
            count = i
            if i - 1 not in numbers:
                while count + 1 in numbers:
                    length += 1
                    count += 1
                if length > longest:
                    longest = length
                length = 1

        return longest
        