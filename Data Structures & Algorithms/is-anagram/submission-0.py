class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of both the string is different than they can't be anagram
        if len(s) != len(t):
            return False
        # case 2: if lengh of both string is same
        char_set = dict() # empty dictonary, since all are lowercase char, max space O(26) ~ O(1)
        for i in range(len(s)):
            # increment char value by one if found in string s
            char_set[s[i]] = 1 + char_set.get(s[i],0)
            # reduce char count val by 1 if found in string t
            char_set[t[i]] = char_set.get(t[i], 0) - 1
        
        # if all char and their count are same then in char_set val we'll get 0
        for key in char_set:
            if char_set[key] != 0:
                return False
        return True

        