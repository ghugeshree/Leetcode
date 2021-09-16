from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output = []
        min_index = 9999

        for restuarant in list1:
            if restuarant in list2:
                test_sum = list1.index(restuarant) + list2.index(restuarant)
                if test_sum < min_index:
                    output.clear()
                    output.append(restuarant)
                    min_index = test_sum
                elif test_sum == min_index:
                    output.append(restuarant)
                    min_index = test_sum

        return output        

test = Solution()
print(test.findRestaurant(["Shogun","Piatti","Tapioca Express","Burger King","KFC"],
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))