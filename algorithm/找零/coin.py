# 问题：
现在有面值1元、2元、5元的零钱无限张，现在给定一个金额，最少的张数组成

# 解决办法：
```
coins = [1, 3, 5]
total = 24
# 这里先算出给定的面值中，最小的面值
min_coins = min(coins)
# 如果都用最小的面值来组合，那么肯定用的张数最多
max_count = total / min_coins + 1

def change_coin():
    # 初始化一个数组来记录不同金额时，需要的最小张数
    # 当金额为0时，张数也为0
    result = [0 for i in range(total+1)]

    for i in range(1, total+1):
        # 最小张数先设定为最多张数
        min_count = max_count
        for j in coins:
            # 分别用不同面值的去计算，先保证金额大于等于此面值
            # 然后取当前金额减去此面值金额时的最小张数 + 1（也就是当前这张）
            # 与设置的最小张数比较，谁小谁就是最小张数
            if i >= j and result[i-j] + 1 < min_count:
                min_count = result[i-j] + 1
        result[i] = min_count
        
    print(result)
    for i in range(total):
        print('凑齐: ', i, '需要: ', result[i])

change_coin()
```
> 这里其实很搞笑，属于为了用动态规划而用，其实这个东西更简单的做法是这样的

```
def change_coin_v2():
    min_count = 0
    surplus = total
    for i in reversed(coins):
        count = surplus // i
        print('凑齐需要 ', i, ' ', count, '张')
        if count <= 0:
            continue
        min_count += count
        surplus = surplus % i
        if surplus <= 0:
            break
    print('最少张数：', min_count)
```
> 想法就是用的张数少，就说明要尽量使用更大面值的，所以就从最大面值，往下算就完事了
