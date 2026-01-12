class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        best_len = float('inf')
        best_start = 0

        for right,ch in enumerate(s):
            if need[ch] >0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                cur_len = right - left + 1
                if cur_len < best_len:
                    best_len = cur_len
                    best_start = left
                # 把 left 移出窗口
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]