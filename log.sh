#!/bin/bash

#Using toggle.txt to check if a debugging-terminal 
#is already open and it doesn't open another one
OUT_FILE="/home/pi/m2i/toggle.txt"
#Logfile
LOG="/home/pi/m2i/log.txt"

#data1 = MIDI Type (Note On)
#data2 = MIDI Value (Note value, see midi_conversion.txt)
data1=$1
data2=$2
note=$(cat midi_conversion.txt | grep $2 | awk '{print $2 $3}')
time=$(date +%Y-%m-%d)
time2=$(date +%T)

#Kill all debug windows
#kill -9 $(pidof xterm)

if [ ! -e ${OUT_FILE} ]; then
	
	
	echo "[$time $time2] Note played: $note" > ${LOG}
	#Debugging-Terminal for Logfile
	#xterm -hold -e cat ${LOG} &
	touch ${OUT_FILE}

else
	
	echo "[$time $time2] Note played: $note" >> ${LOG}
	#Debugging-Terminal for Logfile
	#xterm -hold -e cat ${LOG} &

fi



