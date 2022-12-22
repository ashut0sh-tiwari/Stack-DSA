"""You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid."""

def calPoints(operations):
        stack = [] #initialising an empty stack
        for op in operations: #looping through the elements
            if op == '+': #if element is equal to + then ecord a new score that is the sum of the previous two scores.
                stack.append(stack[-1]+stack[-2])
            elif op == 'D': #if element is equal to D then Record a new score that is the double of the previous score.
                stack.append(stack[-1]*2)
            elif op == 'C': #if element is equal to C then Invalidate the previous score, removing it from the record.
                stack.pop()
            else: #if element is equal to x then Record a new score of x. 
                stack.append(int(op))

        return sum(stack) #returning the sum of the stack
