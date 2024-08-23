# Даны две строки s и t. Верните true,
# если они отличаются ровно на одну операцию редактирования, иначе верните false.

"""
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
"""

class Solution:
    def isOneEditDistance(self, s: "str", t: "str") -> "bool":
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t, s)
        if nt - ns > 1:
            return False
        
        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1 :] == t[i + 1 :]
                else:
                    return s[i:] == t[i + 1 :]
        return ns + 1 == nt
    
if __name__ == "__main__":
    instance = Solution()
    s = "ab"
    t = "acb"
    print(instance.isOneEditDistance(s, t))  # Результат будет напечатан в консоль
