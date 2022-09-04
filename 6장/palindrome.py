import collections


a = "A man, a plan, a canal: panama"


# 내 풀이
# isalnum을(힌트받음) 이용해서 전처리 후 슬라이싱을 이용함(힌트얻음)
def palindrome(strs):
    strs_revise = ''
    for i in strs:
        if i.isalnum():
            strs_revise  += i
    strs_revise  = strs_revise.lower()
    return strs_revise == strs_revise[::-1]



# 교재 풀이
# 1. 데크 자료형
def is_palindrome(s):
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# 2. 슬라이싱 사용 - 1보다 2배 빠름
import re
def is_palindrome2(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


