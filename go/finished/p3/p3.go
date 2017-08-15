package main

import (
    "fmt"
    "math"
)

func is_prime(x int) bool{
  n := int(math.Ceil(math.Sqrt(float64(x))))
  i := 2
  if x == 2 {
    return true
  }

  for i <= n {
    if x % i == 0 {
        return false
    }

    i += 1
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
