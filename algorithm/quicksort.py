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
            left += 1
            while left < right and numbers[left] < key:
                left += 1
            numbers[right] = numbers[left]
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
