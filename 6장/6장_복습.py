# 1. 유효한 팰린드롬
import re

a = "A man, a plan, a canal: panama"
def palindrome(strs):
    new_strs = strs.lower()
    new_strs = re.sub(r'[a-z0-9]', '', new_strs)

    return new_strs[::-1] == new_strs


# 2. 문자열 뒤집기
a = ['h','e','l','l','o']

def reverse_strs(strs):
    strs.reverse()


# 3. 로그 파일 재정렬
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def reorder_log_file(logs):
    letters = []
    digits = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


# 4. 가장 흔한 단어
import re
import collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def most_common_word(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                                    .lower().split()
                                    if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


# 5. 그룹 애너그램
strs = ["eat","tea","tan","ate","nat","bat"]

def anagram(strs):
    anagrams = collections.defaultdict(strs)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagram.values())


# 6. 가장 긴 팰린드롬 부분 문자열
def longest_palindrom(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 and s == s[::-1]:
        return s

    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
