#!/usr/bin/python3
# Bit of code that produces fake sensor data
### OBS: the script takes two arguments: 
# The data contains time stamp and some random number.

import datetime;
import random
import sys
import csv
#from csv import reader
from time import sleep

# amount of lines to generate
#arg1 = sys.argv[1]
#name of csv
#arg2 = sys.argv[2]

def new_row():
    # produce increasing time
        # ct stores current time
    ct = str(datetime.datetime.now())
    #print("current time:-", ct) # format: 2020-07-15 14:30:26.159446

    #produce random number in range 1 000 000 - 9 999 999
    num = random.randint(1000000,9999999)

    row = [ct,num]
    return row

def write_csv_file(amount, name_of_csv_file):
    # open the file in the write mode
    with open('./'+name_of_csv_file, 'w', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        for i in range(int(amount)):
            row = new_row()
            # write a row to the csv file
            writer.writerow(row)

    # close the file
    f.close()

#test loop
def loop_em():
    with open("sensor_data.csv", newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)
            res = do_calculation(int(row[1]))
            print("RES: "+ str(res))
# test calc
def do_calculation(num):
    ran = random.randint(10,99)
    sleep(0.5)
    return num % ran
#print("Generating a csv file with "+arg1+"lines, named: "+arg2)
#write_csv_file(10, "sensor_data.csv")
#loop_em()


