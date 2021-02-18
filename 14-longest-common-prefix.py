class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        new = sorted(strs)
        str1 = new[0]
        str2 = new[-1]
        l = min(len(str1),len(str2))
        common = ""
        for i in range(0,l):
            if str1[i]==str2[i]:
                common+=str1[i]
            else:
                return common
        return common  