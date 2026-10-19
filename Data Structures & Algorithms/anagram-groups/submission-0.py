from collections import defaultdict
class Solution:
    def isAnagrams(self, str1: List[str], str2: List[str]) -> bool:
        if len(str1) != len(str2):
            return False
        temp = {}
        for i in range(len(str1)):
            temp[str1[i]] = temp.get(str1[i], 0) + 1
            temp[str2[i]] = temp.get(str2[i], 0) - 1
        for key in temp:
            if temp[key] != 0:
                return False
        return True

    def groupAnagrams_optimize_bruteforce(self, strs: List[str]) -> List[List[str]]:
        result = []
        i = 0
        while i <= len(strs)-1:
            temp_list = [strs[i]]
            for j in range(i+1, len(strs)):
                if self.isAnagrams(strs[i], strs[j]):
                    temp_list.append(strs[j])
                    strs[i+1], strs[j] = strs[j], strs[i+1]
                    i = i+1
            i = i+1
            result.append(temp_list)
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            result[tuple(freq)].append(s)
            
        return list(result.values())




            

                    

        