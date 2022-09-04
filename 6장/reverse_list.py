a = ['h','e','l','l','o']


# 문자열 뒤집기
# 내 방법
def reverse_list(a):
    print(a[::-1])


# 1. 투 포인터를 이용한 swapping
def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 2. 파이썬 다운 방법
def reverseString2(s):
    s.reverse()