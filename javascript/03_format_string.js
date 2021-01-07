// 6 kyu

/*
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
// returns 'Bart'

list([])
// returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
*/

function list(names) {
    let output = "";
    names.forEach(function (item, index) {
        output = output.concat(item.name, ', ');
    })
    output = output.substring(0, output.length - 2);
    let pos = output.lastIndexOf(',')
    if (pos > 1) {
        return output.substring(0, pos) + ' &' + output.substring(pos + 1)
    } else {
        return output
    }
}

/* 
Most clever
*/
function list(names) {
    // create an array with the names
    var xs = names.map(p => p.name)
    // remove the last element (change the length of xs!!!)
    var x = xs.pop()
    // join the values together with the last one being an ampersand
    // or return the single name or and empty string
    // (for an array of a single vaue, join method return the value without doing anything)
    return xs.length ? xs.join(", ") + " & " + x : x || ""
}


////////////////////////////////////////////////////////////////////////////////////
//  TESTING
////////////////////////////////////////////////////////////////////////////////////
class Test {
    static assertEquals(func, answer) {
        func == answer ? console.log('\x1b[32m%s\x1b[0m', 'Test Passed') : console.log('\x1b[31m%s\x1b[0m', 'Test Failed');
    }
}

Test.assertEquals(list([{ name: 'Bart' }, { name: 'Lisa' }, { name: 'Maggie' }, { name: 'Homer' }, { name: 'Marge' }]), 'Bart, Lisa, Maggie, Homer & Marge',
    "Must work with many names")
Test.assertEquals(list([{ name: 'Bart' }, { name: 'Lisa' }, { name: 'Maggie' }]), 'Bart, Lisa & Maggie',
    "Must work with many names")
Test.assertEquals(list([{ name: 'Bart' }, { name: 'Lisa' }]), 'Bart & Lisa',
    "Must work with two names")
Test.assertEquals(list([{ name: 'Bart' }]), 'Bart', "Wrong output for a single name")
Test.assertEquals(list([]), '', "Must work with no names")