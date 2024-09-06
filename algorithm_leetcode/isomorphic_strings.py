# Даны две строки s и t, определите, являются ли они изоморфными.
# Две строки s и t являются изоморфными, если символы в s могут быть заменены для получения t.

"""
Input: s = "egg", t = "add"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True
    
if __name__ == "__main__":
   isIsomorphic = Solution()
   result = Solution.isIsomorphic(isIsomorphic, s = "egg", t = "add")
   print(result)