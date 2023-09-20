def is_palindrome(s: str) -> bool:
    return False if len(s) == 0 else s == s[::-1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2 and is_palindrome(s):
            return s

        maximum = s[:2] if is_palindrome(s[:2]) else s[0]
        for i in range(1, len(s) - 1):
            cur_string = s[i]
            k = 1

            while i - k >= 0 and i + k < len(s):
                cur_string = s[i - k] + cur_string + s[i + k]
                k += 1
                if is_palindrome(cur_string):
                    maximum = max(maximum, cur_string, key=len)
                else:
                    break

            k = 1
            cur_string = s[i] + s[i + 1]
            maximum = max(maximum, cur_string, key=len) if is_palindrome(cur_string) else maximum

            while i - k >= 0 and i + k + 1 < len(s):
                cur_string = s[i - k] + cur_string + s[i + k + 1]
                k += 1
                if is_palindrome(cur_string):
                    maximum = max(maximum, cur_string, key=len)
                else:
                    break

        return maximum
