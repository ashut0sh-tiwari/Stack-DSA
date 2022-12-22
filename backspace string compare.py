"""Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty."""

s = "ab##"
t = "c#d#"

def backspaceCompare(s,t):
        stack1 =[] #initialising the variables
        stack2 =[] #initialising the variables
        for i in s: #looping string1
            if i == '#': #if found # and stack is not empty then pop last element from the stack
                if stack1 != []:
                    stack1.pop()
            else: #else append that character into the stack
                stack1.append(i)

        for j in t: #looping string2
            if j == '#':#if found # and stack is not empty then pop last element from the stack
                 if stack2 != []:
                    stack2.pop()
            else: #else append that character into the stack
                stack2.append(j)#else append that character

        if stack1 == stack2: #if both stacks are equal return true else false
            return True
        else:
            return False

solution = backspaceCompare(s,t)
print(solution)