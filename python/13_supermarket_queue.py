'''
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
'''


def queue_time(customers, n):
    '''
    my solution
    '''
    queue = [0] * n
    time = 0
    while True:
        for i in range(0, n):   # manage each queue
            if queue[i] == 0:  # empty queue
                if customers:  # still some customers
                    queue[i] = customers.pop(0)
                else:   # no more customers
                    if max(queue) <= 0:
                        return time
            queue[i] -= 1
        time += 1


def queue_time(customers, n):
    '''
    best solution
    - create "n" empty queues
    - iterate through the customers
        - assign next customer to the queue with the minimum amout of person
    '''
    queue = [0] * n
    for i in customers:
        queue[queue.index(min(queue))] += i
    return max(queue)


def queue_time(customers, n):
    '''
    best solution refactored with explanation
    '''
    queue = [0] * n
    for customer in customers:
        # find the queue with the minimum amout of customer
        min_queue = min(queue)
        # get the index of that queue
        index_queue = queue.index(min_queue)
        # add the next customer to that queue
        queue[index_queue] += customer
    # get the length of the biggest queue
    max_queue = max(queue)
    return max_queue


if __name__ == "__main__":
    print(str(queue_time([], 1)) + ' expected 0')
    print(str(queue_time([5], 1)) + ' expected 5')
    print(str(queue_time([2], 5)) + ' expected 2')
    print(str(queue_time([1, 2, 3, 4, 5], 1)) + ' expected 15')
    print(str(queue_time([1, 2, 3, 4, 5], 100)) + ' expected 5')
    print(str(queue_time([2, 2, 3, 3, 4, 4], 2)) + ' expected 9')
    print(str(queue_time([2, 2, 3, 3, 4, 4], 3)) + ' expected 7')
