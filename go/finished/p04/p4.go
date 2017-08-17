package main

import (
    "fmt"
    "strconv"
)

func main() {
  largest := 0
  for i := 1; i < 999; i++ {
    NEXT: for j := i; j < 999; j++ {
      temp :=  i * j
      if temp > largest{
        str := strconv.Itoa(temp)
        for i := 0; i < len(str) / 2 ; i = i+1 {
           if str[i] != str[ len(str) - i - 1 ] {
             continue NEXT
           }
        }
        largest = temp
      }
    }
  }
  fmt.Println(largest)
}
