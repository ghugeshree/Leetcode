/**
 * 7. Reverse Integer
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
 var reverse = function (x) {
    let min = Math.pow(2, 31);
    let max = min - 1;
    min = -min;
    let remainder, reversed = 0, res;
    let signed = 1;
    if (x < 0) {
      signed = -1;
      x = x * signed;
    }
  
    while (x.toString().length - 1 >= 1) {
      remainder = x % 10;
      reversed += remainder * Math.pow(10, x.toString().length - 1);
      x = ~~(x / 10);
    }
    remainder = Math.abs(x % 10);
    reversed = remainder * Math.pow(10, x.toString().length - 1) + reversed;
    reversed = reversed * signed;
  
    if(min < reversed && reversed < max) {
      res = reversed;
    } else {
      res = 0;
    }
    return res; 
  };