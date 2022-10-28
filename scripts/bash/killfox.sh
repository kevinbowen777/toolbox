#!/bin/bash

#{{{ ======================================================================= #
# Author: Kevin Bowen <kevin.bowen@gmail.com>
# Script Name: killfox.sh
# Description:
#		  Identify first firefox process & kill it
# 
# Created: 202221016
# Last modified: 20221027
# Dependencies:
#	None
#}}} ======================================================================= #

ps -ef | grep firefox | awk 'NR==1 {print $2}' | xargs kill
