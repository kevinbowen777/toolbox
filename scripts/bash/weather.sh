#!/bin/bash

#{{{ ======================================================================= #
# Author: Kevin Bowen <kevin.bowen@gmail.com>
# Script Name: weather.sh
# Description:
#   Pull weather data from wttr.in
#
# Created: 2018?
# Last modified: 20221027
# Dependencies:
#	None
#}}} ======================================================================= #

clear
date
curl -s wttr.in/bothell | head -7
