'''
Create a     that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.

Priority:
()
* /
+ _
'''
    
import operator
    
class Calculator(object):
    op_mul = { '*': operator.mul, '/': operator.floordiv}
    op_som = {'+': operator.add, '-': operator.sub}
    tot = 0
    
    def evaluate(self, string):
        string = string.split()
        while len(string) > 1:
            string = self.calc_par(string)
        return float(string[0])
         
    def calc_par(self, string):
        if '(' in string:
            start = string.index('(') + 1
            end = len(string) - string[::-1].index(')') - 1
            return string[:start-1]+self.calc_par(string[start:end])+string[end+1:]
        else:
            return self.calc_mul(string)
        
    def calc_mul(self, string):
        if '*' in string or '/' in string:
            i = 0
            while i < len(string):
                if string[i] in self.op_mul:
                    total = self.op_mul[string[i]](float(string[i-1]),float(string[i+1]))
                    string[i-1] = total
                    string.pop(i+1)
                    string.pop(i)
                else:
                    i += 1
        ret = self.calc_som(string)
        return ret
        
    def calc_som(self, string):
        if '+' in string or '-' in string:
            i = 0
            while i < len(string):
                if string[i] in self.op_som:
                    total = self.op_som[string[i]](float(string[i-1]),float(string[i+1]))
                    string[i-1] = total
                    string.pop(i+1)
                    string.pop(i)
                else:
                    i += 1
        return string

if __name__ == "__main__":
    import codewars_test as test
    test.assert_equals(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
    test.assert_equals(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
    test.assert_equals(Calculator().evaluate('1 + 1'), 2)
    test.assert_equals(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
    test.assert_equals(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
    test.assert_equals(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
    test.assert_equals(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)
    test.assert_equals(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"), 8)