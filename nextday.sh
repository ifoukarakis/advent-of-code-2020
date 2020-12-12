#! /bin/bash

mkdir day$1
touch day$1/input.txt
touch day$1/example.txt

cat <<EOT >> day$1/solve.py
FILENAME = 'example.txt'
# FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

EOT

