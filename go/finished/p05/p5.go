package main

import (
  "fmt"
  "math"
)

func isprime(p int) bool {
  n := int(math.Ceil(math.Sqrt(float64(p))))
  if p == 2 { return true }
  for i := 2; i <= n; i++ {
    if p % i == 0 { return false }
  }
  return true
}

func main(){
  var primes []int // primes := make([]int, 0) // primes := []int{}
  var powers []int
  var composites[]int
  prod := 1
  for i := 2; i <= 20; i++ {
    if isprime(i) {
      primes = append(primes, i) } else {
      composites= append(composites, i) }
  }
  for i := 0; i<len(primes); i++ {
    powers = append(powers, 1)
  }
  for _, c := range composites {
    for i, p := range primes {
      if c % p == 0 {
        for count := 1; c != 1; count++ {
          c = int( c / p)
          if powers[i] < count { powers[i] = count }
        }
      }
    }
  }
  for i, pow := range powers {
    prod = prod * int(math.Pow(float64(primes[i]), float64(pow)))
  }
  fmt.Println(prod)
}
