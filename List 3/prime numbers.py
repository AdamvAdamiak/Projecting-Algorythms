from math import sqrt


f_global = [2]


def czp(p): # 1.1
    f = f_global[0]
    if p < f:
        return []
    if p % f == 0:
        return [f] + czp(p / f)
    f += 1
    f_global[0] = f
    return czp(p)


def start_end(start, end): # 1.2
    result = []
    while start != end+1:
        result.append(start)
        start += 1
    return result


def sera(p): # 1.2
    sq = int(sqrt(p))
    current = 1
    tab = start_end(1, p)
    while True:
        if current > sq:
            return tab

        for i in tab:

            if (not(i % current) and not(current == i)) and current != 1:
                tab.remove(i)

        i = tab.index(current)+1
        current = tab[i]


print(czp(30))
print(sera(30))
