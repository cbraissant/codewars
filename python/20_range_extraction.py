'''
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''
def solution(args):
    string = str(args[0])
    # iterate through each element
    j = 1
    while j < len(args):
        
        # add a new number if not consecutive
        if args[j] - args[j-1] > 1:
            string += ',' + str(args[j])
                
        # find consecutive numbers
        if args[j] - args[j-1] <= 1:
            string += '-'
            while args[j] - args[j-1] <=1:
                # check if end of numbers
                if j < len(args)-1:
                    j += 1
                else:
                    string += str(args[j])
                    return string
            else:
                # add the last number
                string += str(args[j-1])
        
        
        j += 1
                
    return string

'''
Verbose solution
- group first number and last number of sequence (even if identical)
- check if number are identical
- check if sequence > 2
'''
def solution(args):
    start = []
    end = []
    string = ''
    for i in range(len(args)):

        # start a new set
        if start == []:
            start.append(args[i])
            end.append(args[i])
            continue
        
        # check if consecutive numbers    
        if args[i] - end[-1] == 1:
            end[-1] = args[i]
        
        else:
            start.append(args[i])
            end.append(args[i])
    
    for i in range(len(start)):
        if end[i] - start[i] == 0:
            string += str(start[i]) + ','

        if end[i] - start[i] == 1:
            string += str(start[i]) + ',' + str(end[i]) + ',' 

        if end[i] - start[i] > 1:
            string += str(start[i]) + '-' + str(end[i]) + ',' 
    return string[:-1]
        

if __name__ == "__main__":
    import codewars_test as Test
    Test.describe("Sample Test Cases")

    Test.it("Simple Tests")
    Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
    Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')