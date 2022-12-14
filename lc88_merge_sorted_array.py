from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total, l1, l2 = m + n - 1, m - 1, n - 1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[total] = nums1[l1]
                total, l1 = total - 1, l1 - 1

            elif nums1[l1] == nums2[l2]:
                nums1[total] = nums2[l2]
                nums1[total - 1] = nums1[l1]
                total, l1, l2 = total - 2, l1 - 1, l2 - 1

            else:
                nums1[total] = nums2[l2]
                total, l2 = total - 1, l2 - 1

        while l2 >= 0:
            nums1[total] = nums2[l2]
            total, l2 = total - 1, l2 - 1


if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
