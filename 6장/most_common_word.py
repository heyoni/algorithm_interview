paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 가장 흔한 단어
# 내 풀이 -> 힌트 유
import re
import collections
def common_word(paragraph, banned):
    l = [word for word in re.sub('[^\w]',' ',paragraph).lower().split(' ') if word not in banned and word != '']

    common_word = collections.Counter(l)
    print(common_word.most_common(1)[0][0])
