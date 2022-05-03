#!/bin/bash

start=$(date +%s%3N)
start1=$(nc time.nist.gov 13)
echo "Actual start time: $start1" >> start_time.txt
var1=1

python3 -m flask run --host=0.0.0.0 > /var/runfile.log 2>&1 &
while [ "$var1" -eq 1 ]
    do 
        ifres=$(grep -i "http" /var/runfile.log | wc -l) 
        if [ $ifres -eq 1 ]
            then
                end2=$(nc time.nist.gov 13)
                echo "Actual end time: $end2" >> start_time.txt
                end=$(date +%s%3N)
                seconds=$(echo "$end - $start" | bc)
                #echo $seconds' sec'
                echo 'Formatted start time of application:' >> start_time.txt
                awk -v t=$seconds 'BEGIN{t=int(t*1000); printf "%d:%02d:%02d:%03d\n", t/3600000, t/60000%60, t/1000%60, t/1000%60}' >> start_time.txt
                var1=0
        fi
    done
var3=3
while [ "$var3" -eq 3 ]
    do
    sleep 1
    done

