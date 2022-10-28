#! /bin/bash

#{{{ ======================================================================= #
# Author: Kevin Bowen <kevin.bowen@gmail.com>
# Script Name: docker_clean.sh
# Description:
#   Clean up intermediate docker images
#
# Created: 20221016
# Last modified: 20221027
# Dependencies:
#	None
#}}} ======================================================================= #

docker image ls | grep none | awk  '{ print $3 }' > results.txt

awk '{cmd="docker rmi " $1; system(cmd)}' results.txt

rm results.txt
