from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        chars_on_row = ["qwertyuiop",
                "asdfghjkl",
                "zxcvbnm"]

        result = []
        for word in words:
            index = 0
            if word[0].lower() in chars_on_row[1]:
                index = 1
            elif word[0].lower() in chars_on_row[2]:
                index = 2
             
            can_form_word = True
            for char in word:
                if char.lower() not in chars_on_row[index]:
                    can_form_word = False
                    break
            
            if can_form_word:
                result.append(word)
        print(result)        

test = Solution()
test.findWords(["adsdf","sfd"])