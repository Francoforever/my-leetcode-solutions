class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        if m == 0:
            nums1 = []
            nums1.extend(nums2)
            return
        if n == 0:
            return
        for a in range(0, m + n):
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                if j == n:
                    break
            if nums1[i] <= nums2[j]:
                i += 1
                if i == m:
                    nums1.extend(nums2[j:])
                    break
        return
