#   Notice:
# 0 is charge and 1 is uncharge

# your command : python directory-of-chargeto.py your-percentage-here
# ex: python /home/son/chargeto.py 80

# you can set alias for "python chargeto.py": 
# echo "alias short-name='python directory-of-chargeto.py'" >> ~/.bash
# then the command : short-name your-percentage-here

import sys,os
import psutil,math
import subprocess,time








class file_path():
    def __init__(self,filename):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(script_directory, filename)
         

class run_cmd():
    def __init__ (self,command):
        try:
            self.result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if self.result.returncode == 0:
                '''print("Command executed successfully.")
                print("Output:")
                print(result.stdout)'''
                
            else:
                print("Error:", self.result.stderr)
        except Exception as e:
            print("An error occurred:", e)
    def get_output(self):
        return self.result.stdout

class set_battery_mode():
    def __init__(self,mode):
        self.output = run_cmd(f"echo {mode}  | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode ")
    def get_mode(self):
        return self.output.get_output()
    
class get_battery_percentage ():         
    def __init__ (self):
        battery_get = psutil.sensors_battery()
        self.percent = battery_get.percent
    def get(self):

        return math.floor(self.percent)
    
class check_plugin():
    def __init__(self,mode):
        if mode == 0 :
            set_battery_mode(0)
            count(5)
        battery_get = psutil.sensors_battery()
        self.plugged = battery_get.power_plugged
    def check(self):
        return self.plugged

class check_battery():
    def __init__(self,bat,x,output):
        if bat >= x and output !=1 :
            output = set_battery_mode(1)
            mode = output.output
            return False,mode
        elif bat <x and output !=0 :
            output = set_battery_mode(0)
            mode = output.output
            return True,mode
        else:
            set_battery_mode(1)
            
            return False
    
class count():
    def __init__ (self,seconds=60):
        for i in range(seconds, 0, -1):
            time.sleep(1)
        
    
class chargeto():
    def __init__ (self,x):
        output = 1
        battery = get_battery_percentage().get()
        check,output = check_battery(battery,x,output)
        while check:
            if x-battery <= 1 : seconds = 30 
            else : seconds = 60
            count(seconds)
            battery = get_battery_percentage().get()
            #print(f"battery : {battery}%")
            check,output = check_battery(battery,x,output)
            if check == False:
                    break
    def get_out(self):
        return self.out
            
if __name__ == "__main__":
    try :
        try:
            x = int(sys.argv[1])
        except:
            x=80
        getbat = get_battery_percentage().get()
        if getbat < x and x<=100:
            set_battery_mode(0)
            #print("Checking...")
            count(5)
            if check_plugin() :
                #print("Pluged")
                #print(f"Charging from {getbat}% to {x}%")
                chargeto(x)
            else:
                set_battery_mode(1)
                #print("Unpluged")
        else:
            '''if getbat == x :
                print(f"Your battery is {getbat}")
            else:
                print(f"Your battery {getbat}% over {x}%")'''
            set_battery_mode(1)
            pass
    except :
        set_battery_mode(1)
        
# 0 is charge and 1 is uncharge

