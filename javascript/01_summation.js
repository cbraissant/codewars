// 8 kyu

/*
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
*/

// Simple and easy solution
let summation = function (num) {
    let total = 0;
    for (i=0; i<=num; i++){
        total += i;
    };
    return total;
}

// Arrow funciton
let summation = n => n*(n+1) / 2

