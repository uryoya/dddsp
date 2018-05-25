#! /bin/bash

n=10
if [ $# -eq 1 ]; then
    n=$1
fi

domains=("chino.org" "cocoa.com" "rize.com" "chia.co.jp" "sharo.net")

for ((i=0; i < $n; i++)); do
    port=$(expr 9000 + $i)
    ./dddsp.out ":$port" ${domains[$(expr $i % 5)]} > log/dsp$i.log 2>&1 &
    echo "Wake up server on $port. PID is $!"
done

echo "Started $n servers."
