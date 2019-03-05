package main

import "fmt"

func main() {
    var a = [...]int{1, 2, 3, 4, 5, 6, 7, 8, 11, 33, 55, 66}
    var b = [...]int{1, 4, 5, 8, 12, 42, 45, 51, 63, 78, 88}
    fmt.Println(a)
    fmt.Println(b)
    var result []int

    var a_len int = len(a)
    var b_len int = len(b)
    var lengths = a_len + b_len
    var a_site int = 0
    var b_site int = 0

    for i := 0; i < lengths; i ++ {
        if a_site >= a_len {
            // 这里不知道go有没有更好的合并列表的办法
            for j := b_site; j < b_len; j ++ {
                result = append(result, b[j])
            }
            break
        }
        if b_site >= b_len {
            for j := a_site; j < a_len; j ++ {
                result = append(result, a[j])
            }
            break
        }
        if a[a_site] <= b[b_site] {
            result = append(result, a[a_site])
            a_site += 1
        } else {
            result = append(result, b[b_site])
            b_site += 1
        }

    }
    fmt.Println(result)
}
