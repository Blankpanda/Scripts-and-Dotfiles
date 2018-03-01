#!/bin/bash

INP=$1
if [[ -d $INP ]]; then # directory
    ls $INP
elif [[ -f $INP ]]; then # file
   cat $INP
else
    echo "Invalid Input"
    exit 1
fi
