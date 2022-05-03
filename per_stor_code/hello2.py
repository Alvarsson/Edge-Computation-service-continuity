from flask import Flask
import subprocess as sp
import datetime
import shlex
from gen_data import *
# TEST EVERYTHING NOW AND SEE IF IT WORKS. WHEN IT DOES, INCREASE SPEED
# AND MAKE TIMESTAMP MORE ACCURATE.

def custom_call():
    id = gen_id()
    while True:
        if data_exist() == (1,0):
            file_name = "log1.txt"
            if is_my_id(id, "1"):
                next_num = generate(get_latest(file_name))
                timestamp = str(datetime.datetime.now())
                output = str(id) +";"+ str(next_num) +";"+ timestamp
                #writing to file 
                sp.call(shlex.split(f"./test1.sh {output}"))
                
            else:
                # maybe generate log2.txt here? ./gen_log2.sh
                sp.call(['sh', './gen_log2.sh'])
                next_num = generate(get_latest(file_name))
                timestamp = str(datetime.datetime.now())
                output = str(id) +";"+ str(next_num) +";"+ timestamp
                #writing to file 2
                sp.call(shlex.split(f"./test2.sh {output}"))
        elif data_exist() == (1,1):
            if is_my_id(id, "1"):
                file_name = "log1.txt"
            else:
                file_name = "log2.txt"
            next_num = generate(get_latest(file_name))
            timestamp = str(datetime.datetime.now())
            output = str(id) +";"+ str(next_num) +";"+ timestamp
            if is_my_id(id, "1"):
                sp.call(shlex.split(f"./test1.sh {output}"))
            else:
                sp.call(shlex.split(f"./test2.sh {output}"))
        else:
            # gen log1.txt here ./gen_log1.sh
            sp.call(['sh', './gen_log1.sh'])
            first_num = generate(0)
            timestamp = str(datetime.datetime.now())
            output = str(id) +";"+ str(first_num) +";"+ timestamp
            sp.call(shlex.split(f"./test1.sh {output}"))


@app.route('/')
def index():
    return "HELLO WORLD!"

custom_call()