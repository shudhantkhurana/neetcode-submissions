class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            num = ord(i.lower())
            if (num >= 97 and num <= 122) or (num >= 48 and num <= 57):
                arr.append(i.lower())

        return arr == arr[::-1]