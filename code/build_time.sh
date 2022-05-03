#!/bin/bash

now=$(date +"%T.%N")
now2=$(nc time.nist.gov 13)
echo "Actual start time of build: $now2" >> start_time.txt
echo "Current time : $now"
echo "Start time of build(one hour of eg. 14 = 15 a clock): $now" >> start_time.txt



#start=$(date +%s)
#end=$(date +%s)

#seconds=$(echo "$end - $start" | bc)
#echo $seconds' sec'

#echo 'Formatted start time of application:' >> start_time.txt
#awk -v t=$seconds 'BEGIN{t=int(t*1000); printf "%d:%02d:%02d\n", t/3600000, t/60000%60, t/1000%60}' >> start_time.txt