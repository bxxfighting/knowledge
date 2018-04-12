package main

import (
    "fmt"
    "time"
    "math/rand"
)

func main() {
    var numbers []int

    timens := int64(time.Now().Nanosecond())
    rand.Seed(timens)

    for i := 0; i < 10; i ++ {
        numbers = append(numbers, rand.Intn(100))
    }
    fmt.Println(numbers)

    quick_sort(numbers, 0, len(numbers)-1)
    fmt.Println(numbers)
}

func quick_sort(numbers []int, left int, right int) {
    if left < right {
        start := left
        end := right
        key := numbers[left]
        for left < right {
            for left < right && numbers[right] > key {
                right --
            }
            numbers[left] = numbers[right]
            left ++
            for left < right && numbers[left] < key {
                left ++
            }
            numbers[right] = numbers[left]
        }
        numbers[right] = key
        quick_sort(numbers, start, right - 1)
        quick_sort(numbers, right + 1, end)
    }
}
