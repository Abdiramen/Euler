package main

import (
    "fmt"
    "math"
)

func is_prime(x int) bool{
  n := int(math.Ceil(math.Sqrt(float64(x))))
  if x == 2 {
    return true
  }

  for i := 2; i <= n; i ++ {
    if x % i == 0 {
        return false
    }
  }

  return true
}

func main(){
  bignum := 600851475143
  i := 3
  biggest := 0
  for bignum != 1 {
    if is_prime(i) {
      if bignum % i == 0 {
        bignum /= i
        biggest = i
      }
    }
    i+=2
  }
  fmt.Println(biggest)
}
