class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        n1_idx = n2_idx = 0
        while n1_idx < len(nums1) or n2_idx < len(nums2):
            if n1_idx == len(nums1):
                merged.extend(nums2[n2_idx:])
                break
            elif n2_idx == len(nums2):
                merged.extend(nums1[n1_idx:])
                break
            elif nums1[n1_idx] < nums2[n2_idx]:
                merged.append(nums1[n1_idx])
                n1_idx += 1
            else:
                merged.append(nums2[n2_idx])
                n2_idx += 1
        if len(merged) % 2 == 0:
            median = float(merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        else:
            median = merged[len(merged) // 2]
        return median
