#!/bin/bash

pid=$(pidof m2i)
kill -9 $pid

if [ -e toggle.txt ]; then	

	rm toggle.txt

fi
