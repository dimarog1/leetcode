class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_symbs = set()
        i = 0
        j = 1
        cur_str = ''
        while len(s) >= j >= i:
            new_str = s[i:j]
            if new_str[-1] not in cur_symbs:
                cur_str = max(cur_str, new_str, key=len)
                cur_symbs.add(new_str[-1])
            else:
                while i < j and s[i] != new_str[-1]:
                    cur_symbs.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return len(cur_str)
