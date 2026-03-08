class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # 1. 初始化 DP 矩阵
        # dp[i][j] 代表 text1[:i] 和 text2[:j] 的 LCS 长度
        # 多出一行一列是为了处理空字符串的情况（边界条件）
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 2. 填充表格
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # 发现匹配字符，斜对角加 1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 不匹配，取上方或左方的最大值
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # 3. 最终结果
        return dp[m][n]

# --- 本地测试 ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("abcde", "ace", 3),    # ace
        ("abc", "abc", 3),      # abc
        ("abc", "def", 0),      # 无
        ("","",0)
    ]
    for t1, t2, expected in test_cases:
        res = sol.longestCommonSubsequence(t1, t2)
        print(f"text1: {t1}, text2: {t2} | 预期: {expected}, 实际: {res}")