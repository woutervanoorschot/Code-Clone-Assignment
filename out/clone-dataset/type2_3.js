const a = [0,1,2,3,4,5,56,67,78,89,9,456,6,4523,4,3];
let b = 0;
for(i = 0; i< a.length; i++){
    if(a[i].toString().includes('5')){
        b++;

    }
}
console.log(b)