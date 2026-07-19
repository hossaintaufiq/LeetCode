class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointer for the last valid element in nums1
        i = m - 1

        # Pointer for the last element in nums2
        j = n - 1

        # Pointer for the last position in nums1
        k = m + n - 1

        # Compare elements from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining elements from nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1