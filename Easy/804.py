from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_map = {
        'a':".-",
        'b':"-...",
        'c':"-.-.",
        'd':"-..",
        'e':".",
        'f':"..-.",
        'g':"--.",
        'h':"....",
        'i':"..",
        'j':".---",
        'k':"-.-",
        'l':".-..",
        'm':"--",
        'n':"-.",
        'o':"---",
        'p':".--.",
        'q':"--.-",
        'r':".-.",
        's':"...",
        't':"-",
        'u':"..-",
        'v':"...-",
        'w':".--",
        'x':"-..-",
        'y':"-.--",
        'z':"--.."}
        
        final_set = set()
        for word in words:
            string = ''
            for alpha in word:
                string = string + morse_code_map.get(alpha)
            final_set.add(string)
        
        print(len(final_set))

test = Solution()
test.uniqueMorseRepresentations(["gin","zen","gig","msg"])