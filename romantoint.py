class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert a roman numeral (string) to equivalent integer
        
        - Can there be invalid numerals (e.g. IIII, ICXV, etc.)?
        + Assuming all inputs are valid Roman numerals
        
        Use a hash table to hold kv pairs
        Loop through and convert each character to its int value, or negative value if conditions are met
        
        For each char in the string
            if the next char is a larger value that is valid to subtract from
                Subtract value from return
            Otherwise
                Add value to return
                
        Runs in O(n), but hash tables are memory intensive
        
        Ways to optimize:
        * 
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        result = 0
        
        # i is index, char is letter
        for i, char in enumerate(s):
            # Last character is always positive
            if i < len(s) - 1:
                # Check next character to see if current one should be negative
                if values[s[i + 1]] > values[char]:
                    result -= values[char]
                else:
                    result += values[char]
            else:
                result += values[char]
                    
        return result