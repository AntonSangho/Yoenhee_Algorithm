class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)
    
solution = Solution()

s1 = "rat"
t1 = "car"
result1 = solution.isAnagram(s1, t1)
print(f"'{s1}'과 '{t1}'은 애너그램인가? {result1}")