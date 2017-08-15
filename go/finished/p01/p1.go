package main

import "fmt"

func main() {
  sum := 0
  for num := 0; num < 1000; num++ {
    if num % 3 == 0 {
      sum += num
    } else if num % 5 == 0 {
      sum += num
    }
  }
  fmt.Println(sum)
}
