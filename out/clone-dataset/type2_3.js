/* Count amount of numbers containing five */
const a = [0, 1, 2, 3, 4, 5, 56, 67, 78, 89, 9, 456, 6, 4523, 4, 3];
let b = 0;
// for loop over array
for (c = 0; c < a.length; c++) {
    if (a[c].toString().includes('5')) {
        // add to count if number includes a five
        b++;
    }
}
// output result
console.log(b)