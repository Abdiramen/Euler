package main

import "fmt"

func fib(max int) int {
  a, b := 1, 0
  sum := 0
  for a < max {
    if a % 2 == 0 {
        sum += a
    }
    a, b = b,a+b
  }
    return sum
}
func main(){
   fmt.Println(fib(4000000))
}
