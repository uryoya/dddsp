#!/bin/bash

h2load -c10 -n500 -p http/1.1 http://localhost:8080/ad -d data.txt

