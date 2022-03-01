/* Count amount of numbers containing five */
const five = [0,
    1,
    2,
    3,
    4,
    5,
    56,
    67,
    78,
    89,
    9, 
    456,
    6,
    4523,
    4,
    3];
let count = 0;
// for loop over array
for (i=0; i<five.length; i++) {
    if (five[i].toString().includes('5')) { count++; }
} console.log(count)