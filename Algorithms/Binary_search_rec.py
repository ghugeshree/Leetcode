from typing import List

class Test:
    def binary_search(self, A: List, target) -> bool:
        print(A)
        i, j = 0, len(A)
        mid = (i + j) // 2

        if len(A) == 1 and A[0] != target:
            return False

        if A[mid] == target:
            return True
        elif A[mid] < target:
            return Test.binary_search(self, A[mid:], target)
        elif A[mid] > target:
            return Test.binary_search(self, A[:mid], target)
                
test = Test()
print(test.binary_search([-1, -2, -3, 0, 4, 5, 6, 7], 0))

        
