class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        l = len(nums1)
        return float(nums1[l//2]+nums1[(l//2)-1])/2 if l%2 == 0 else nums1[(l-1)//2]
