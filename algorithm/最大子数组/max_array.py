# 问题：
有一个数组，里面有正数与负数，现在想取任意连续的数字相加，如何得到最大和
# 解决办法：
```
nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(nums)

def find_max_sub_array():
    start = 0
    end = 0
    # 初始化一个数组来记录结果，当一个数字都不取时，最大和为0
    result = [0 for i in range(len(nums)+1)]
    # 记录最大和使用，初始时，记录结果数组中的第一个，也就是一个数字都不取时
    max_value = result[0]
    for i in range(1, len(nums)):
        # 当结果集中记录的值为小于等于0的数时，那么和这个数相加，只能使数更小
        # 所以就不要这之前算过的了，重新开始
        if result[i-1] <= 0:
            result[i] = nums[i-1]
            start = i - 1
        else:
            result[i] = result[i-1] + nums[i-1]
        # 如果当前结果大于以前保存的最大值，则重新保存为最大值
        if result[i] > max_value:
            max_value = result[i]
            end = i - 1
    print('start: ', start)
    print('end: ', end)
    print('max: ', max_value)


find_max_sub_array()
```
结果：
```
[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
start:  7
end:  10
max:  43
```
