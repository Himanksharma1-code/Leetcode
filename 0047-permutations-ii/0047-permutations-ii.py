import itertools


class Solution:

  def permuteUnique(self, nums):
    return [list(p) for p in set(itertools.permutations(nums))]