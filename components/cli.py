#from colors import * #import all from colors.py module
#from git import * #import all from colors.py module
import os
import sys

#The split method return an array with the head and the tail of the path
path= os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.split(os.path.realpath(__file__))[1]

if os.path.exists(path+"/functions.py"): 
    from components.functions import *

#Cli
def cli():
   command=""
   while command!="exit":
         command = input("\n\033[1;32mInput: ")
         if case(command)==False:
            print(RED, "Error: command unknown")
           

        # #...
        # if command == "help":
        #     help()
        # elif command == "modules":
        #     show_modules()
        # elif command == "version":
        #     show_version()
        # elif command == "clear":
        #     print("\033c")
        # #commands module
        # if "commands" in command:
        #     if command == "commands user":
        #         commands.user_commands()
        #     elif command == "commands network":
        #         commands.network_commands()
        #     elif command == "commands filesystem":
        #         commands.filesystem_commands()
        #     elif command == "commands system":
        #         commands.system_commands()
        #     else:
        #         commands.show()
        # #bash module
        # if command == "bashrc":
        #     bashrc.show() 
        # #docker module
        # if "docker" in command:
        #     if "docker list" in command:
        #         docker.list()
        #     elif "docker description" in command:
        #         docker.show_description()
        #     elif "docker configuration" in command:
        #         docker.show_configuration()
        #     elif "docker about" in command:
        #             docker.show_about()
        #     elif "docker in" in command:
        #             docker.show_in()
        #     elif "docker images" in command:
        #             docker.show_images()
        #     elif "docker containers" in command:
        #         docker.show_containers()
        #     elif "docker network" in command:
        #         docker.show_network()
        #     elif "docker volumes" in command:
        #             docker.show_volumes()
        #     elif "docker dockerfile" in command:
        #             docker.show_dockerfile()
        #     else:
        #         docker.show()
        


