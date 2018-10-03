#!/bin/sh

while inotifywait -r -e modify .
  do
    clear
    python3 awsconsol.py ec2
    mypy -m 
  done
