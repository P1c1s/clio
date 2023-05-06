from colors import * #import all from colors.py module
import os
import sys

#The split method return an array with the head and the tail of the path
path= os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.split(os.path.realpath(__file__))[1]

if os.path.exists(path+"/../modules/apt.py"):
    from modules import apt 
    enabled_modules=["apt"]
if os.path.exists(path+"/../modules/bashrc.py"): 
    from modules import bashrc 
    enabled_modules+=["bashrc"]
if os.path.exists(path+"/../modules/commands.py"):
    from modules import commands
    enabled_modules+=["commands"]
if os.path.exists(path+"/../modules/docker.py"):
    from modules import docker
    enabled_modules+=["docker"]
if os.path.exists(path+"/../modules/iptables.py"):
    from modules import iptables
    enabled_modules+=["iptables"]
if os.path.exists(path+"/../modules/git.py"):
    from modules import git
    enabled_modules+=["git"]
if os.path.exists(path+"/../modules/rsync.py"):
    from modules import rsync 
    enabled_modules=["rsync"]


#List of available modules
available_modules=["apt", "bashrc", "commands", "docker", "git", "iptables", "rsync"]

#Manager Function 
def about():
    print("Clio is a helper for linux users which helps to remember linux commands easly")
    print("It's written in python. It was built with a modular architecture.")
    print("Where each module can be added or removed in any time.")
    print("Each module can work standalone.\n", RED)
    print("        | <- components")
    print("        |")
    print("        |            | <- module[1]")
    print("core <- | <- modules | <- module[2]")
    print("        |            | <- module[n]")
    print("        |")
    print("        | <- ...\n", WHITE)
def clear():
    print("\033c")
def exit():
    print("Bye, bye")
def help(bool):
    print(WHITE, "Usage: clio [COMMAND]")
    print(WHITEBOLD, "about", WHITE, "      -  Show you some information about Clio")
    if bool:
        print(WHITEBOLD, "clear", WHITE, "      -  Clear the terminal screen")
    if not bool:
        print(WHITEBOLD, "cli", WHITE, "        -  Lunch Clio in command line mode")
    if bool:
        print(WHITEBOLD, "exit", WHITE, "       -  Exit from command line mode")
    print(WHITEBOLD, "help", WHITE, "       -  Display information about Clio commands")
    print(WHITEBOLD, "info", WHITE, "       -  Show information about modules")
    print(WHITEBOLD, "modules", WHITE, "    -  Show enabled and not enabled modules")
    print(WHITEBOLD, "unknow", WHITE, "     -  ...")
    print(WHITEBOLD, "version", WHITE, "    -  Show the version of Clio")
def info():
    #for module in enabled_modules:
        print("commands")
        commands.list()
        if "apt" in enabled_modules:
            print("apt")
            apt.list()
        if "docker" in enabled_modules:
            print("docker")
            docker.list()
        if "git" in enabled_modules:
            print("git")
            git.list()
def show_modules():
    print("MODULES")
    for module in available_modules:
      if module in enabled_modules:
          print(GREENBOLD, "[+]", module)
      else:
          print(REDBOLD, "[-]", module)
def show_version():
    print("v0.1")
def unknow():
    print("d")

#######
def funzione1(argn, argw):
    if len(sys.argv) > argn: #compare the lenght of array with the number of input!!!
        if sys.argv[argn] == argw:
          return True

#nome da rivedere
def case(command):
    #...
    if command == "about":
        about()
        return True
    elif command == "clear":
        clear()
    elif command == "exit":
        exit()
        return True
    elif command == "help":
        help(True)
        return True
    elif command == "modules":
        show_modules()
        return True
    elif command == "version":
        show_version()
        return True
    elif command == "unknow":
        unknow()
        return True
    #commands module
    if "commands" in command:
        if command == "commands user":
            commands.user_commands()
            return True
        elif command == "commands console":
            commands.console_commands()
            return True
        elif command == "commands network":
            commands.network_commands()
            return True
        elif command == "commands filesystem":
            commands.filesystem_commands()
            return True
        elif command == "commands system":
            commands.system_commands()
            return True
        else:
            commands.show()
            return True
    #bash module
    if command == "bashrc":
        bashrc.show() 
        return True
    #docker module
    if "docker" in command:
        if "docker list" in command:
            docker.list()
            return True
        elif "docker description" in command:
            docker.show_description()
            return True
        elif "docker configuration" in command:
            docker.show_configuration()
            return True
        elif "docker about" in command:
            docker.show_about()
            return True
        elif "docker in" in command:
            docker.show_in()
        elif "docker images" in command:
            docker.show_images()
            return True
        elif "docker containers" in command:
            docker.show_containers()
            return True
        elif "docker network" in command:
            docker.show_network()
            return True
        elif "docker volumes" in command:
            docker.show_volumes()
            return True
        elif "docker dockerfile" in command:
            docker.show_dockerfile()
            return True
        else:
            docker.show()
            return True
    return False

#file
def write(string):
  with open('DB_data.dat', 'a') as f:
    f.write('{} {}\n'.format(1,sys.argv[2],))
def load():
  with open('DB_data.dat', 'r') as f:
      line = f.readline()
      data = []
      while line:
          data.append(line.split(' '))
          line = f.readline()
  print(data)
def read():
  with open('DB_data.dat', 'r') as f:
      print(f.read())
      

def delete(row):
  with open('DB_data.dat', 'r') as f:
    line = f.readline()
    data = []
    while line:
        data.append(line.split(' '))
        line = f.readline()
    print(data)
    line.remove('1')
    print(data)
        
    
