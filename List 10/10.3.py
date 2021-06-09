s = 'jakiślosowytekst'
dictionary = ['jakiś', 'jabłko', 'ogórek', 'tekst', 'banan', 'losowy']
r = []
max_l = len(max(dictionary, key=len))
for j in range(1, len(s) + 1):
    i = j - 1
    flag = 0
    ans = []
    x = 0
    # Letting setting x to j - max_l optimization,
    # the code will work even if x is always set to 0
    if j > max_l:
        x = j - max_l
    while i >= x:
        if s[i:j] in dictionary:
            if i > 0 and r[(i - 1)]:
                # appending the word to all the valid sentences
                # formed by the substring ending at i-1
                temp = list((map(lambda x: x + " " + s[i:j], \
                                 r[(i - 1)])))
                for elem in temp:
                    ans.append(elem)
                flag = 2
            else:
                flag = 1
                r.append([s[i:j]])
        i = i - 1
    # if the substring does not belong to the
    # dictionary append an empty list to result
    if flag == 0:
        r.append([])
    if flag == 2:
        r.append(ans)
if s in dictionary:
    r[len(s) - 1].append(s)

for i in range(len(s)):
    print(f'string: "{s[:(i + 1)]}", result [{i}]: {r[i]}')
# If result[len(s)-1] is empty then the string cannot be
# broken down into valid strings
print("Found:", r[len(s) - 1])