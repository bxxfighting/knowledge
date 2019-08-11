import random

def quick_sort(numbers, left, right):
    if left < right:
        start = left
        end = right
        key = numbers[left]
        while left < right:
            while left < right and numbers[right] > key:
                right -= 1
            numbers[left] = numbers[right]
            # 这里这个left += 1可以不要，如果写了的话
            # 在2号位标识之后，都应该使用right，而不能用left
            # 如果把这个left += 1去掉的话，2号位标识之后的地方
            # 可以用left也可以用right
            left += 1
            while left < right and numbers[left] < key:
                left += 1
            numbers[right] = numbers[left]
        # 2号位
        numbers[right] = key
        quick_sort(numbers, start, right - 1)
        quick_sort(numbers, right + 1, end)


def gen_rand_numbers(numbers_size):
    numbers = [random.randint(1, 100) for i in range(numbers_size)]
    return numbers

if __name__ == "__main__":
    numbers = gen_rand_numbers(10)
    print(numbers)
    quick_sort(numbers, 0, len(numbers)-1)
    print(numbers)
