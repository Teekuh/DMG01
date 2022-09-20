#!/bin/bash

i=0

winid=$(xdotool search "move_circle")
echo $winid

time=5e-1
sleep 1

while true; do

sleep $time
echo c$i 
xdotool key --window ${winid}--delay 10 $i+c
sleep $time
echo c#$i
xdotool key --window ${winid}--delay 10 $i+k
sleep $time
echo d$i 
xdotool key --window ${winid}--delay 10 $i+d
sleep $time
echo d#$i
xdotool key --window ${winid}--delay 10 $i+b
sleep $time
echo e$i
xdotool key --window ${winid}--delay 10 $i+e
sleep $time
echo f$i
xdotool key --window ${winid}--delay 10 $i+f
sleep $time
echo f#$i
xdotool key --window ${winid}--delay 10 $i+v
sleep $time
echo g$i
xdotool key --window ${winid}--delay 10 $i+g
sleep $time
echo g#$i
xdotool key --window ${winid}--delay 10 $i+p
sleep $time
echo a$i
xdotool key --window ${winid}--delay 10 $i+a
sleep $time
echo a#$i
xdotool key --window ${winid}--delay 10 $i+o
sleep $time
echo h$i
xdotool key --window ${winid}--delay 10 $i+h

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
