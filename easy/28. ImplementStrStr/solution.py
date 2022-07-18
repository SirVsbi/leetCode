class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = 0
                temp = i
                while haystack[i] == needle[j]:
                    j += 1
                    i += 1
                    if j == len(needle):
                        return temp
                    if i == len(haystack):
                        return -1
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert (solution.strStr("hello", "ll") == 2)
    assert (solution.strStr("aaaaa", "bba") == -1)
    assert (solution.strStr("aasdasdsdfgds", "") == 0)
    assert (solution.strStr("aaaaal", "ll") == -1)
