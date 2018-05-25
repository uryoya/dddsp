#!/bin/bash

for ((i=1000; i<=10000; i+=1000)); do
    h2load -c100 -n$i -p http/1.1 http://localhost:8080/ad -d data.txt
    echo ""
    sleep 10
done
