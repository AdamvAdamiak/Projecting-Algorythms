import itertools
items = [(2, 40), (2, 160), (3, 70), 
(15, 300), (1, 70), (4, 25),
         (5, 25), (6, 180),
          (3, 80), (4, 180), 
          (5, 120), (1, 50), (3, 70)]



def knapsackr(items, weight):
    n = len(items)
    lst = [list(i) for i in itertools.product([0, 1], repeat=n)]
    accept_sol_vec = []
    accept_sol_value = []
    for vector in lst:
        sum_w = 0
        sum_p = 0
        for i in range(n):
            if vector[i] == 1:
                sum_w += items[i][0]
                sum_p += items[i][1]

        if sum_w <= weight:
            accept_sol_vec.append(vector)
            accept_sol_value.append(sum_p)

    max_p = 0
    for i in range(len(accept_sol_value)):
        if accept_sol_value[i] > max_p:
            max_p = accept_sol_value[i]

    return max_p

if __name__ == '__main__':
    print('Wartość przedmiotów metodą zachłanną: ', knapsackr(items, 700))
