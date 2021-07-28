result = []
def solution(result):
    s = input()
    i = s[::-1]
    temp = ''
    res = []
    abc = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1, 27)))
    for letter in i:
        temp = letter*abc[letter.lower()]
        res.append(temp)
    result.append(''.join(res))
t = int(input())
[solution(result) for j in range(t)]
[print(n) for n in result]