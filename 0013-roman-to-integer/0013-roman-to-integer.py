class Solution:
    def romanToInt(self, s):
        # Map of Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the string from right to left
        for char in reversed(s):
            value = roman_map[char]
            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                # Otherwise, add it
                total += value
            prev_value = value
        
        return total