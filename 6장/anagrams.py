strs = ["eat","tea","tan","ate","nat","bat"]


# 그룹 애너그램
# 내 풀이
import collections
def group_anagrams(strs):
    new_strs = [] 
    for i in strs:
        new_strs.append(collections.Counter(i))

    result = [[var] for var in strs]
    for i in range(len(strs)):
        for j in range(i+1,len(strs)-1):
            if new_strs[i] == new_strs[j]:
                result[i].append(strs[j])

    print(result)


# 애너그램 -> "정렬"하여 비교하기(와우..)
# 정렬한 값을 키값으로 하는 딕셔너리 만들기
def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)
    for s in strs:
        anagrams[''.join(sorted(s))].append(s)

    return list(anagrams.values())

print(groupAnagrams(strs))