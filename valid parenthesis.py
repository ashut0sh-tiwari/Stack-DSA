"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""


s ="{[()]}"


def isValid(s):
        brackets = {")" : "(",  "}" : "{", "]" : "["} #dictionary to match parenthesis
        stacked = [] #empty stack
        for i in s: #looping through the string
            if i in brackets.values(): #if element is in brackets value i.e opening parenthesis then append that in stacked
                stacked.append(i)
            elif stacked and brackets[i] == stacked[-1]: #if element is in brackets i.e closing parenthesis then checking if stacked is empty or not(it can be checked by typing stacked only or stacked is empty) and if not then checking if that matches with top most stacked element if yes then pop the element from the stacked
                stacked.pop()

            else: #else return false
                return False
        return True if not stacked else False #returning true if stacked is empty otherwise false

solution = isValid(s)
print(solution)