#!/usr/bin/env python3
import chargeto_background as cb
import os,subprocess

    



def avoid_pass(path):
    username = os.getlogin()
    
    command = f"/usr/bin/python3 {path}"

    # Construct the command to modify the sudoers file
    sudoers_command = f'echo "{username} ALL=(ALL) NOPASSWD: {command}" | sudo tee -a /etc/sudoers'

    # Execute the command to modify the sudoers file
    proc = subprocess.Popen(sudoers_command, shell=True)
    proc.wait()


def is_file_modified(file_path):
    current_time = os.path.getmtime(file_path)
    previous_time = os.path.getatime(file_path)

    if current_time > previous_time:
        return True
    else:
        return False 


def get_num():
    file_path = cb.file_path("config.txt")
    config_file_path = file_path.file_path   
    try :
        with open(config_file_path, "r") as file:
            number = int(file.read().strip())
    except:
        number = 80
    if number >99:
        number = 100
    return number
## trong file setup, rerun file autorun if change number trong file config.txt
avoid_pass(cb.file_path("autorun.py").file_path)
number = get_num()
mode = 0
try :
    while True:
        print("run...")
        cb.count(5)
        if is_file_modified(cb.file_path("config.txt").file_path):
            number = get_num()
        if (mode == 1) and (cb.get_battery_percentage().get() < number)   : mode =0
        if (cb.check_plugin(mode).check()) :
            if(cb.get_battery_percentage().get() >= number) and (mode == 0):
                cb.set_battery_mode(1)
                mode = 1
            else:
                try :
                    mode = cb.chargeto(number).get_out()
                except :
                    cb.set_battery_mode(1)
            mode == 3
        
except:
        if (cb.get_battery_percentage().get() >= number):
            cb.set_battery_mode(1)  




