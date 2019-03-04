n = 10
c = 50
cl = [2, 11, 5, 17, 8, 14, 7, 9, 10, 12]
vl = [4, 8, 1, 14, 9, 3, 21, 6, 7, 10]


def pack():
    # 创建一个表，来记录不同背包容量不同矿石个数时，对应的价值
    # 初始化为0主要是因为我们假设没有矿石或者没有容量时，那么价值就是0
    table = [[0 for i in range(n+1)] for j in range(c+1)]
    for i in range(1, c + 1):
        # 假设在同容量下，不同矿石个数时，取最高价值
        for j in range(1, n + 1):
            # 当增加一块矿石时，先判断总容量够不够放下它自己的
            # 然后在当前容量下减去这块矿石的体积，取出对应的价值
            # 再加上当前矿石的价值后进行比较
            if i >= cl[j-1] and table[i-cl[j-1]][j-1] + vl[j-1] > table[i][j-1]:
                table[i][j] = table[i-cl[j-1]][j-1] + vl[j-1]
            else:
                table[i][j] = table[i][j-1]
    return table

def print_max(table):
    # 最后一个存储的一定是最大价值
    print('max: ', table[c][n])


def print_choiced(table):
    # 准备一个列表来存储哪个矿石被选中，选中就标识为1
    l = [0 for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if table[j][i] > table[j][i-1]:
            l[i-1] = 1
            print('选择了第 ', i, ' 块矿石', '体积：', cl[i-1], '价值：', vl[i-1])
            j -= cl[i-1]

r = pack()
print_max(r)
print_choiced(r)
