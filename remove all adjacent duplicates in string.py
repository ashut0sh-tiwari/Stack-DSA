"""You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique."""

s = "abbaca"

def removeDuplicates(string):
        stacked = [] #making an empty stack
        for i in s: #looping every element
            if stacked and stacked[-1] == i: #if stack is not empty and last element of stack is equals to i element then pop it from the stack
                stacked.pop()
            else:
                stacked.append(i) #else append that element in the stack

        return "".join(stacked) #joining the stack with empty character to make it a string and returning it

solution = removeDuplicates(s)
print(solution)