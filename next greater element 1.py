"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above."""


nums1 = [4,1,2]
nums2 = [1,3,4,2]
def nextGreaterElement(list1, list2): #function to find the next greater element from the list
        nums1Idx = {n:i for i,n in enumerate(list1)} #initialising the dict variable with index and value of list 1
        res = [-1] * len(list1) #initialising the array variable with elements equal to list 1 with value -1
        stack = [] #initialising the stack

        for i in range(len(list2)): #looping through the list 2 
            cur = list2[i] #storing the value of index i in cur variable
            while stack and cur > stack[-1]: #if stack is not empty and cur value is greater than stack top
                val = stack.pop() #pop the stack top and store the value in val
                idx = nums1Idx[val] #find the index of the val from the dict and storing in variable
                res[idx] = cur #updating the res value with cur value at given index
            if cur in nums1Idx: #if cur also exist in list 1
                stack.append(cur) #adding that value in stack

        return res #returning res


solution = nextGreaterElement(nums1, nums2)
print(solution)