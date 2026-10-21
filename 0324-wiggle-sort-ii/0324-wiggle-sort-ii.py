class Solution(object):
    def wiggleSort(self, nums):
        arr = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2
        nums[::2] = arr[:mid][::-1]
        nums[1::2] = arr[mid:][::-1]