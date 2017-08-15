package main

import "fmt"

func main() {
  num := 0
  sum := 0
  for num < 1000 {
    if num % 3 == 0 {
      sum += num
    } else if num % 5 == 0 {
      sum += num
    }
    num += 1
  }
  fmt.Println(sum)
}
