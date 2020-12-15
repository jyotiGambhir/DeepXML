#!/usr/bin/env bash

python3 /content/DeepXML/main.py --data-cnf /content/DeepXML/configure/datasets/EUR-Lex.yaml --model-cnf /content/DeepXML/configure/models/AttentionXML-EUR-Lex.yaml -t 0
# python3 main.py --data-cnf /content/DeepXML/configure/datasets/EUR-Lex.yaml --model-cnf /content/DeepXML/configure/models/AttentionXML-EUR-Lex.yaml -t 1
# python3 main.py --data-cnf /content/DeepXML/configure/datasets/EUR-Lex.yaml --model-cnf /content/DeepXML/configure/models/AttentionXML-EUR-Lex.yaml -t 2
# python3 ensemble.py -p results/$2-$1 -t 3

