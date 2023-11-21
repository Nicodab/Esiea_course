#!/bin/sh
INFO=$(sudo docker container ls -f ancestor=ssh1 -q)
if [ "X$INFO" != "X" ]; 
then
  sudo docker stop $INFO
fi
sudo docker build --rm -t ssh1 .
sudo docker run -d --read-only -p 12221:22 ssh1:latest
