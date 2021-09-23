from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        counter = 0 
        is_set = False

        for char in s:
            if char == c:
                counter = 0
                is_set = True
            elif not is_set:
                counter = 1001   
            else:
                counter += 1
            result.append(counter)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                counter = 0
            else:
                counter += 1
            result[i] = min(result[i], counter)

        print(result)
             

test = Solution()
test.shortestToChar(s = "aaaab", c = "b")