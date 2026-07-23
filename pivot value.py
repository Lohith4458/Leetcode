class Solution:
    def pivotIndex(self, nums):
        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        total = prefix[-1]

        for i in range(n):
            left_sum = prefix[i - 1] if i > 0 else 0
            right_sum = total - prefix[i]

            if left_sum == right_sum:
                return i

        return -1


nums = [1, 7, 3, 6, 5, 6]

obj = Solution()
print("Pivot Index =", obj.pivotIndex(nums))