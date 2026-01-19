#Inside this python file we will read the log file and print the necessary information in terminal and output file
#To activate debugger, Import pdb (python debugger)
#readlines() itself is a list type(file.readlines())

import json

"""
#1st Method to read the log file
def read_logs_using_open():
    file = open("app.log","r")
    print(file.readlines())
    file.close()
    
#2nd Method to read the log file
def read_logs_using_with_open():
    with open("app.log","r") as file:
        print(file.readlines())

    """

def read_logs_using_with_open():
    lines = []
    with open("app.log","r") as file:
        return (file.readlines())
    
def log_analyze(lines):
    log_count = {
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO": log_count["INFO"]+1})
        elif "WARNING" in line:
            log_count.update({"WARNING": log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR": log_count["ERROR"]+1})
        else:
            pass
    return log_count

def write_logs_into_file(log_counts):
    with open("log_summary.json","w+") as json_file:
        json.dump(log_counts,json_file,indent=4)


lines = read_logs_using_with_open()
log_counts = log_analyze(lines)
write_logs_into_file(log_counts)