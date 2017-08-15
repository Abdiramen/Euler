#!/bin/bash
a="1"
b="0"
temp="0"
sum=0
while [ $a -lt 4000000 ]
  do
    echo "$a  $b"
    if !(($a % 2))
        then
          sum=$[$sum+$a]
    fi
    temp=$a
    a=$[$a+$b]
    b=$[$temp]
  done
echo $sum
