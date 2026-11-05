class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False
        if target == 0:
            return True

        a, b = x, y
        while b:
            a, b = b, a % b

        return target % a == 0

    canMeasureWaterCapacity = canMeasureWater