import random
from os.path import exists
# generate some data based on previous data
def generate(start):
    if start == 0:
        data = 1
    else:
        data = start + 1
    return data

# generate random id of specific length
def gen_id():
    id = random.randint(1000000,9999999)
    return id

#check if data exist, maybe check if file exist already?
def data_exist():
    source = 0
    dest = 0
    if exists("/mnt/log1.txt"): # check source file
        source = 1
    if exists("/mnt/log2.txt"): # check dest file
        dest = 1
    return (source,dest)
    

# check if id is this applications id
def is_my_id(id, file_num):
    #gather id, read from file
    file_name = "/mnt/log" + file_num + ".txt"
    with open(file_name, 'r') as f:
        last_line = f.readlines()[-1]

    log_data = last_line.split(";")[0]
    if int(log_data) == id:
        return True
    return False

#
def get_latest(file_name):
    path = "/mtn/" + file_name
    with open(file_name, 'r') as f:
        last_line = f.readlines()[-1]
    latest_num = last_line.split(";")[1]
    return int(latest_num)