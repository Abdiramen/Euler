package main

import (
  "fmt"
  "log"
)

func main() {
  var n int
  fmt.Print("give N: ")
  _, err := fmt.Scanf("%d", &n)
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println((3 * n * n * n * n + 2 * n * n * n - 3 * n * n  - 2 * n) / 12)
}
