// 8 kyu

/* 
Write a function called repeat_str which repeats the given string src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
*/

function repeatStr(n, s) {
    return s.repeat(n)
}

// same with arrow function
const repeatStr = (n, s) => s.repeat(n)