#!/usr/bin/env bash

python3 main.py --data-cnf configure/datasets/$1.yaml --model-cnf configure/models/$2-$1.yaml -t 0
python3 main.py --data-cnf configure/datasets/$1.yaml --model-cnf configure/models/$2-$1.yaml -t 1
python3 main.py --data-cnf configure/datasets/$1.yaml --model-cnf configure/models/$2-$1.yaml -t 2
python3 ensemble.py -p results/$2-$1 -t 3
