
import chargeto_background as cb
import sys,os,subprocess
LOGINPASSWD = "20012003"

def script_path():
    return os.path.dirname(os.path.abspath(__file__))
    

def file_path(filename):
    script_directory = script_path()
    file_path = os.path.join(script_directory, filename)
    return file_path

file_path1 = file_path("config.txt")
config_file_path = file_path1   
with open(config_file_path, "r") as file:
    number = int(file.read().strip())

def add_to_starup (name,command):

    # Specify the name and command for the startup program

    # Create the desktop entry file content
    desktop_entry = f"""[Desktop Entry]
    Type=Application
    Name={name}
    Exec={command}
    """
    
    # Specify the path where the desktop entry file will be saved
    desktop_entry_path = os.path.expanduser(f"~/.config/autostart/{name}.desktop")

    # Write the desktop entry file
    with open(desktop_entry_path, "w") as file:
        file.write(desktop_entry)


def avoid_pass(path):
    username = os.getlogin()
    
    command = f"/usr/bin/python3 {path}"

    # Construct the command to modify the sudoers file
    sudoers_command = f'echo "{username} ALL=(ALL) NOPASSWD: {command}" | sudo tee -a /etc/sudoers'

    # Execute the command to modify the sudoers file
    proc = subprocess.Popen(sudoers_command, shell=True)
    proc.wait()
    
class setup():
    def __init__(self):
        print(":")

    def get_num (self):
        file_path = cb.file_path("config.txt")
        config_file_path = file_path.config_file_path
        try :   
            with open(config_file_path, "r") as file:
                number = int(file.read().strip())
        except: 
            number = 80
        return number
    def cthold(num):
        with open(config_file_path, "w") as file:
           file.write(str(num)) 
    
    
    "python -c 'from setup import setup; setup.cthold(42)'"

if __name__ == "__main__":
    file_set_up = "setup.py"
    file_autorun = "autorun.py"

    try:
        a = sys.argv[1]
        
        if a == "-h":
            print("If you want to change percentage, type 'cthold new-number'")
        else :
            cb.run_cmd(f"cd {script_path()} \n python -c 'from setup import setup; setup.cthold({a})'")
        #x = setup.get_num()
        #cb.run_cmd(f"pkill -f {file_path("autorun.py")}")
        #atr.autorun(x,True)
    except:
        
        avoid_pass(file_path(file_autorun))
        add_to_starup("Run autorun.py",f" echo {LOGINPASSWD} | sudo -S /usr/bin/python3 {file_path(file_autorun)} &")
        add_to_starup("Run test.py",f" echo {LOGINPASSWD} | sudo -S /usr/bin/python3 {file_path(file_set_up)} &")
        cb.run_cmd(f"echo \"alias cthold='python {file_path(file_set_up)}'\" >> ~/.bashrc")
        cb.run_cmd(f"echo \"alias setup='python {file_path(file_set_up)}'\" >> ~/.bashrc")
        cb.run_cmd(f"echo \"alias autorun='python {file_path(file_autorun)} '\" >> ~/.bashrc")

        #x=setup.get_num()
        #atr.autorun(x,True)
        
        print("type 'setup -h' to get help")
        print("please run cmd: 'source ~/.bashrc'")
        print("run cmd: 'autorun to run code every reboot system")
        
    
            