#!/bin/bash

i=0

winid=$(xdotool search "move_circle")
echo $winid

time=5e-1
sleep 1

while true; do

sleep $time
echo c$i 
echo c$i > ./current_value.txt
sleep $time
echo c#$i
echo c#$i > ./current_value.txt
sleep $time
echo d$i 
echo d$i  > ./current_value.txt
sleep $time
echo d#$i
echo d#$i > ./current_value.txt
sleep $time
echo e$i
echo e$i > ./current_value.txt
sleep $time
echo f$i
echo f$i > ./current_value.txt
sleep $time
echo f#$i
echo f#$i > ./current_value.txt
sleep $time
echo g$i
echo g$i > ./current_value.txt
sleep $time
echo g#$i
echo g#$i > ./current_value.txt
sleep $time
echo a$i
echo a$i > ./current_value.txt
sleep $time
echo a#$i
echo a#$i > ./current_value.txt
sleep $time
echo h$i
echo h$i > ./current_value.txt

i=$((i+1))

if [ "$i" = "10" ] ; then
i=0
fi

done
#i=$((i+1))
#touch file${i}.txt
#xdotool key --window ${winid}--delay 10 Up
#sleep $time
#xdotool key --window ${winid}--delay 10 Right
#sleep $time
#xdotool key --window ${winid}--delay 10 Down
#sleep $time
#xdotool key --window ${winid}--delay 10 Leftf3
#sleep $time
#done

#echo "Press any key --window ${winid}--delay 10 to continue"
#while [ true ] ; do
#read n
#if [ $n = "a" ] ; then
#xdotool key --window ${winid}--delay 10 f+2 
#elif [ $n = "w" ] ; then
#xdotool key --window ${winid}--delay 10down +$ixffea
#xdotool key --window ${winid}--delay 10 f
#xdotool key --window ${winid}--delay 10 2
#xdotool key --window ${winid}--delay 10up +$ixffea
#elif [ $n = "s" ] ; then
#xdotool key --window ${winid}--delay 10 f+3 
#elif [ $n = "d" ] ; then
#xdotool key --window ${winid}--delay 10down +$ixffea
#xdotool key --window ${winid}--delay 10 f
#xdotool key --window ${winid}--delay 10 3
#xdotool key --window ${winid}--delay 10up +$ixffea
#else
#echo "waiting for the key --window ${winid}--delay 10press"
#fi
#done
