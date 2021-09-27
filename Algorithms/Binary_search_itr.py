from typing import List

class Test:
    def binary_search(self, A: List, target) -> bool:
        i, j = 0, len(A)
        mid = (i + j) // 2
        while i < j:
            if A[mid] < target:
                i = mid
            elif A[mid] > target:
                j = mid
            elif A[mid] == target:
                return True
            else:
                mid = (i + j) // 2      
            return False 
                
test = Test()
print(test.binary_search([1,2,3,4,5,6,7], 10))

        
