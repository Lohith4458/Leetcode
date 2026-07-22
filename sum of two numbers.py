class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            index = seen.get(target - num)

            if index is not None:
                return [index, i]

            seen[num] = i
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 17))