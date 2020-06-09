#!/bin/bash

pipenv run python main.py &

while true
do
    sleep 60

    echo "Add Drop All"
    iptables -I INPUT -j DROP

    sleep 60

    echo "Remove Drop All"
    iptables -D INPUT -j DROP

done