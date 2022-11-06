class Solution:
    def removeDuplicates(self, nums):
        length = 0
        if len(nums) == 0: return length
        for i in range(1, len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length + 1


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 6, 6, 6, 7, 8, 10]
    r = Solution()
    numberOfUniqueElements = r.removeDuplicates(nums)
    print('unique elements cnt %s ' %(numberOfUniqueElements))
    print('Result list %s ' %nums)
