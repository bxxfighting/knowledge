package main

import "fmt"

type statement func(d date) bool

type date [2]int

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

func month(d date) int {
    return d[0]
}

func day(d date) int {
    return d[1]
}

func know(dates []date) bool {
    if len(dates) == 1 {
        return true
    }
    return false
}

func tell_m(m int, dates []date) []date {
    var sdates []date

    for i := 0; i < len(dates); i ++ {
        if dates[i][0] == m {
            sdates = append(sdates, dates[i])
        }
    }
    return sdates
}

func tell_d(d int, dates []date) []date {
    var sdates []date

    for i := 0; i < len(dates); i ++ {
        if dates[i][1] == d {
            sdates = append(sdates, dates[i])
        }
    }
    return sdates
}

func hear(dates []date, statements ...statement) []date {
    var sdates []date
    for i := 0; i < len(dates); i ++ {
        result := true
        for _, stmt := range statements {
            result = result && stmt(dates[i])
        }
        if result {
            sdates = append(sdates, dates[i])
        }
    }

    return sdates
}

func a1(d date) bool {
    var after_being_told = tell_m(month(d), dates)
    result := true
    for i := 0; i < len(after_being_told); i ++ {
        result = result && !know(tell_d(day(after_being_told[i]), dates))
    }

    return !know(after_being_told) && result
}

func b1(d date) bool {
    after_tell_d := tell_d(day(d), dates)
    return !know(after_tell_d) && know(hear(after_tell_d, a1))
}

func a2(d date) bool {
    return know(hear(tell_m(month(d), dates), b1))
}

func main() {
    fmt.Println(hear(dates, a1, b1, a2))
}
