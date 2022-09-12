# 가장 긴 팰린드롬 부분 문자열
def longestPalindrom(s):
    # 문자열 발견 시 더 긴 문자열이 있는지 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    # 슬라이딩 윈도우 우측으로 이동(문자열 발견하기)
    for i in range(len(s)-1):
        result = max(result,
                    expand(i, i+1),
                    expand(i, i+2),
                    key=len)    