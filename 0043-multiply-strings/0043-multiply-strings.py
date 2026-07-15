class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        
        for i in range(len1 - 1, -1, -1):
            digit1 = ord(num1[i]) - 48
            for j in range(len2 - 1, -1, -1):
                digit2 = ord(num2[j]) - 48
                
                pos1 = i + j
                pos2 = i + j + 1
                
                total_sum = digit1 * digit2 + result[pos2]
                
                result[pos2] = total_sum % 10
                result[pos1] += total_sum // 10
                
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
            
        return "".join(map(str, result[start:]))