# 两个有序的数组，合并成一个有序数组
a = [1, 3, 4, 5, 6, 33, 56, 66, 99]
b = [1, 2, 3, 44, 55, 64, 111, 123, 133, 344]

print(a)
print(b)
def merge(a, b):
    results = []
    a_len = len(a)
    b_len = len(b)
    lengths = len(a) + len(b)
    a_site = 0
    b_site = 0
    for i in range(lengths):
        # 如果有一个数组已经循环结束了，
        # 那么就直接将另一个数组剩下的值依次写到结果中就可以了
        if a_site >= a_len:
            results += b[b_site:]
            break
        if b_site >= b_len:
            results += a[a_site:]
            break
        # 先从a取数据，如果小于b当前的数据就追加到结果集，同时a当前位置加1
        # 要不然就将b中的数据追加到结果集，同时b当前位置加1
        if a[a_site] <= b[b_site]:
            results.append(a[a_site])
            a_site += 1
        else:
            results.append(b[b_site])
            b_site += 1
    return results

if __name__ == '__main__':
    result = merge(a, b)
    print(result)
