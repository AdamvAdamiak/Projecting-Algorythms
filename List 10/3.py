if __name__ == '__main__':
    s = 'ogórekszpinakparmezan'
    dictionary = ['szpinak', 'jabłko', 'ogórek', 'tekst', 'banan', 'parmezan']
    r = []
    max_l = len(max(dictionary, key=len))
    for j in range(1, len(s) + 1):
        i = j - 1
        flag = 0
        ans = []
        x = 0
        if j > max_l:
            x = j - max_l
        while i >= x:
            if s[i:j] in dictionary:
                if i > 0 and r[(i - 1)]:
                    temp = list((map(lambda x: x + " " + s[i:j],
                                     r[(i - 1)])))
                    for elem in temp:
                        ans.append(elem)
                    flag = 2
                else:
                    flag = 1
                    r.append([s[i:j]])
            i = i - 1
        if flag == 0:
            r.append([])
        if flag == 2:
            r.append(ans)
    if s in dictionary:
        r[len(s) - 1].append(s)

    for i in range(len(s)):
        print(f'tekst: "{s[:(i + 1)]}", rezultat [{i}]: {r[i]}')
    print("Znaleziono:", r[len(s) - 1])
