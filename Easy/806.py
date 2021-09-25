from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        map_of_alpha = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26,
        }
        lines = 1
        total = 0
        for char in s:
            index = map_of_alpha[char]
            total += widths[index - 1]
            if total > 100:
                total = 0
                total += widths[index - 1]
                lines += 1
                
        return [lines, total]   

# using ord() is a faster solution 
# Python ord() function returns the Unicode code from a given character. This function accepts a string of unit length as an argument and returns the Unicode
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lc=1
        tot=0
        for i in s:
            tot+=widths[ord(i)-97]
            if (tot>100):
                tot=widths[ord(i)-97]
                lc+=1
        return [lc,tot]

test = Solution()
print(test.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))