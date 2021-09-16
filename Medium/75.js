/**
 * 75. Sort Colors
 * 
 * This solution is solved using the Dutch National Flag Algorithm.
 * 
 * Conditions of this algorithm:
 *   elements(array[0...low]) = 0
 *   elements(array[low...high]) = 1
 *   elements(array[high...n]) = 2
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * 
 */
let input_array = [2, 0, 2, 1, 1, 0]

function main() {
  let low, mid, high;
  low = mid = 0;
  high = input_array.length - 1;

  while (mid <= high) {
    switch (input_array[mid]) {
      case 0:
        swap(low, mid);
        low++;
        mid++;
        break;

      case 1:
        mid++;
        break;

      case 2:
        swap(mid, high);
        high--;
        break;
    }
  }
  console.log(input_array);
}

function swap(i, j) {
  let temp = input_array[i];
  input_array[i] = input_array[j];
  input_array[j] = temp;
}

main()