#!/bin/sh
script=$1
name=${script%.sh}
chmod +x $script
cp $script /usr/bin/$name
