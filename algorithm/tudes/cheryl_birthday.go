package main

import (
    "fmt"
    "math/rand"
    "time"
)

type date [2]int
type statement func(d date) bool

/*
var dates = []date{
    {5, 15},
    {5, 16},
    {5, 19},
    {6, 17},
    {6, 18},
    {7, 14},
    {7, 16},
    {8, 14},
    {8, 15},
    {8, 17},
}
*/

var dates []date

func gen_dates() []date{
    var some_dates []date
    ms := []int{3, 4, 5, 6, 7}
    d1s := []int{1, 2}
    d2s := []int{5, 6, 7, 8, 9}
    for i := 0; i < len(ms); i ++ {
        for j := 0; j < len(d1s); j ++ {
            for k := 0; k < len(d2s); k ++ {
                var d = date{ms[i], d1s[j]*10+d2s[k]}
                some_dates = append(some_dates, d)
            }
        }
    }
    return some_dates
}

func random_sample(some_dates []date, count int) []date {
    rand.Seed(time.Now().UnixNano())
    var selected_dates []date
    for i := 0; i < count; i ++ {
        j := rand.Intn(len(some_dates))
        selected_dates = append(selected_dates, some_dates[j])
        some_dates = append(some_dates[:j], some_dates[j+1:]...)
    }
    return selected_dates
}

func month(d date) int {
    return d[0]
}

func day(d date) int {
    return d[1]
}

func tell_m(m int) []date {
    var selected_dates []date
    for i := 0; i < len(dates); i ++ {
        if m == dates[i][0] {
            selected_dates = append(selected_dates, dates[i])
        }
    }
    return selected_dates
}

func tell_d(d int) []date {
    var selected_dates []date
    for i := 0; i < len(dates); i ++ {
        if d == dates[i][1] {
            selected_dates = append(selected_dates, dates[i])
        }
    }
    return selected_dates
}

func know(ds []date) bool {
    if len(ds) == 1 {
        return true
    }
    return false
}

func hear(ds []date, statements ...statement) []date {
    var selected_dates []date
    for i := 0; i < len(ds); i ++ {
        result := true
        for _, stmt := range statements {
            result = result && stmt(ds[i])
        }
        if result {
            selected_dates = append(selected_dates, dates[i])
        }
    }
    return selected_dates
}

func a1(d date) bool {
    var after_being_told = tell_m(month(d))
    result := true
    for i := 0; i < len(after_being_told); i ++ {
        result = result && !know(tell_d(day(after_being_told[i])))
    }
    return !know(after_being_told) && result
}

func b1(d date) bool {
    at_first := tell_d(day(d))
    return !know(at_first) && know(hear(at_first, a1))
}

func a2(d date) bool {
    return know(hear(tell_m(month(d)), b1))
}

func main() {
    var some_dates = gen_dates()
    dates = random_sample(some_dates, 10)
    fmt.Println(dates)
    fmt.Println(hear(dates, a1, b1, a2))
}
