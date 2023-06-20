/*
Goal: Parse a body of text, and see how much one can chop of the endings of words without losing distinction between them

e.g.
John went to the market
would become
J e to th m

but on a longer text:
When we went to the market, we didn't know where we were really going
would become
when we wen to th m we d k wher we wer r g
*/
package main

import (
    "fmt"
    "os"
    "strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {

    dat, err := os.ReadFile("example.txt")
    check(err)
    fmt.Print(string(dat))
    fmt.Println("---")
    whole := string(dat)
    each := strings.Split(strings.ToLower(strings.ReplaceAll(whole, "\n"," ")), " ")
    for i, s1 := range each {
        if len(s1) < 1 {
            continue
        }
        word := s1[:1]
        for j, s2 := range each {
            if i == j || s1 == s2{
                continue
            }
            for k := 1; k < len(s1) && k < len(s2); k++ {
                sub1 := s1[:k]
                sub2 := s2[:k]
                if sub1 != sub2 {
                    break
                }
                if sub1 == sub2 && len(word) <= k {
                    word = s1[:k+1]
                }
            }

            //fmt.Println(i, j, s1, s2)
        }
        fmt.Printf("%s ", word)
    }
}
