class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        
        for paren in s:
            if len(my_stack) == 0:
                my_stack.append(paren)
            elif paren in ["[" , "{" , "("]:
                my_stack.append(paren)
            elif (my_stack[len(my_stack) - 1] == "[" and paren == "]") or (my_stack[len(my_stack) - 1] == "{" and paren == "}") or (my_stack[len(my_stack) - 1] == "(" and paren == ")"):
                my_stack.pop()
            else:
                return False
        if len(my_stack) == 0:
            return True

solution = Solution()
print(solution.isValid(""))