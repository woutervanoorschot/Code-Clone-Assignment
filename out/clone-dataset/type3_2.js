/* Count amount of numbers containing five */
const numbers = [0,1,2,3,4,5,56,67,78,89,9,456,6,4523,4,3];
let count = 0;
const length = numbers.length
// for loop over array
for(i = 0; i< length; i++){
    if(numbers[i].toString().includes('5')){
        count++;
    }
}
console.log(count)