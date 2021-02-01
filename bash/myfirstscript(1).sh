#!/bin/bash
#this script demos different types of echo commands

greeting="This is a script. Hello!"
echo $greeting, thanks for joining us!
echo '$greeting, thanks for joining us! YOu owe me $20'
echo "$greeting, thanks for joining us!"
echo "$greeting, you owe me $20"

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME
