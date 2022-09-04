# 로그파일 재정렬 
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# 내 풀이
def reorder_log(logs):
    new_logs = []
    for i in logs:
        new_logs.append(i.split(' '))

    if new_logs[1].isalpha():
        pass


# 람다와 +연산자 이용하기
def reorderLogFiles(logs):
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    print(letters, digits)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


reorderLogFiles(logs)