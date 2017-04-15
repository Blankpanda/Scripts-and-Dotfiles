#!/bin/sh
for var in "$@"
do
    echo "backing up $var"
    sleep 2
    cp --verbose -r $var /backup/
done

