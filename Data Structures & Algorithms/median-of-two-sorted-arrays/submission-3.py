class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right= len(nums1) 
        m, n = len(nums1), len(nums2)

        while left<= right:
            i = (left + right) // 2  # elements from nums1
            j = (m + n + 1) // 2 - i  # elements from nums2
    
            nums1_left = nums1[i-1] if i > 0 else float("-infinity")
            nums1_right = nums1[i] if i < m else float("infinity")
            nums2_left = nums2[j-1] if j > 0 else float("-infinity")
            nums2_right = nums2[j] if j < n else float("infinity")
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # valid partition!
                if (m + n) % 2 == 1:  # odd
                    return max(nums1_left, nums2_left)
                else:  # even
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
            
        