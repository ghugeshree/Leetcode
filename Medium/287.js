/**
 * 287. Find the Duplicate Number
 * 
 * In this solution, I learnt using a Set in js.
 * Set has apis such as: .add(), .delete(), .clear(), .has(), .size(), etc
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n - 1) => O(n)
 */

let input_array = [1, 3, 4, 2, 2]

function findDuplicate() {
  let mySet = new Set();

  for (let i = 0; i < input_array.length; i++) {
    if (mySet.has(input_array[i])) {
      return input_array[i];
    } else {
      mySet.add(input_array[i]);
    }
  }
};

function main() {
  console.log(findDuplicate());
}

main()