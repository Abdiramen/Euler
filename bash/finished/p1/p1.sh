#!/bin/bash
let val=0
for i in {1..999}
  do
    if !(($i % 3))
      then
        let val=val+i
    elif !(($i % 5))
      then
        let val=val+i
    fi
  done

echo $val
