class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {']':'[','}':'{',')':'('}
        for i in s:
            if i in ['[','{','(']:
                stack.append(i)
                print(stack)
            else:
                if len(stack)>0 and keys[i]==stack[-1]: 
                    stack.pop()
                    print(stack)
                else: 
                    return False

        if len(stack) == 0:
            return True
        return False

        