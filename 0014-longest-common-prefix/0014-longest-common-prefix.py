class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_str = min(strs)
        max_str = max(strs)
        
        common_prefix = []
        
        for i, char in enumerate(min_str):
            if i < len(max_str) and char == max_str[i]:
                common_prefix.append(char)
            else:
                break
        
        return "".join(common_prefix)
