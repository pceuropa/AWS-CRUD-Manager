#!/bin/sh

export TESTMODE=1
clear
echo 'Test mode on' 

while inotifywait -r -e modify ..
#while inotifywait -r -e modify ./telemetry
  do
    clear
    ipython3 runner.py
  done
