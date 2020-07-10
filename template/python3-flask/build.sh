#!/bin/bash
DATE=`date +%Y%m%d%H%M%S`
DOCKER_IMAGE=lihodocker/faas-python3-gunicorn:$DATE

cmd="docker build -t $DOCKER_IMAGE ."
echo $cmd
eval $cmd
