#!/usr/bin/env python
import itertools
import time
from flask import Flask, Response, redirect, request, url_for
from create_sensor_data import *
import random
from csv import reader
from datetime import datetime
app = Flask(__name__)

write_csv_file(1000, "sensor_data.csv")

@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            i = 1 
            #for row in range(1000):
            # new below
            while True: 
                now = datetime.now().time() # time object

                #print("now =", now)
                next = read_next(i)
                # new below
                computed = do_calculation(int(next[1]))
                yield "data: %s %d \n\n" % (next, computed)
                # new below
                #yield "computed: %s\n\n" % (computed)
                time.sleep(0.1)  # an artificial delay
                # new below
                i += 1
                if i >= 980:
                    i = 1
                
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))
if __name__ == '__main__':
    app.run()

# Make some random calculation of an input number
def do_calculation(num):
    ran = random.randint(10,99)
    #sleep(0.5)
    return num % ran

#read line by line
def read_next(i):
    with open("sensor_data.csv", newline='') as f:
    # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(f)
        row = list(csv_reader)
        return row[i]

