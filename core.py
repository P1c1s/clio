#from colors import * #import all from colors.py module
#from git import * #import all from colors.py module
import os
import sys

#The split method return an array with the head and the tail of the path
path= os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.split(os.path.realpath(__file__))[1]
#import components
if os.path.exists(path+"/components/functions.py"): 
    from components.functions import *
if os.path.exists(path+"/cli.py"): 
    from components.cli import *
path= os.path.split(os.path.realpath(__file__))[0]
if os.path.exists(path+"/components/guide.py"): 
    from components.guide import *

#Not work
if funzione1(0,"main.py"):
    about()
    print("d")

#Call Manager Function
if len(sys.argv)<2:
    print("Hi, I am Clio. How can I help you?")

#Manager
if funzione1(1,"about"):
    about()
if funzione1(1, "cli"):
    cli()
if funzione1(1, "guide"):
    guide()
if funzione1(1,"help"):
   help(False)
if funzione1(1,"info"):
    info()
if funzione1(1,"modules"):
   show_modules()
if funzione1(1, "unknow"):
    unknow()
if funzione1(1,"version"):
   show_version()
#Manager file
if funzione1(1, "write"):
    write(sys.argv[1])
if funzione1(1, "load"):
    load()
if funzione1(1, "read"):
    read()
if funzione1(1, "delete"):
    delete(sys.argv[2])

if funzione1(1, "apt"):
    apt.show()
if funzione1(1, "commands"):
    if funzione1(2, "about"):
        commands.about()
    elif funzione1(2,"user"):
        commands.user_commands()
    elif funzione1(2,"console"):
        commands.console_commands()
    elif funzione1(2,"network"):
        commands.network_commands()
    elif funzione1(2,"filesystem"):
        commands.filesystem_commands()
    elif funzione1(2,"system"):
        commands.system_commands()
    else:
        commands.show()
if funzione1(1, "bashrc"):
    bashrc.show() 
if funzione1(1, "docker"):
    if funzione1(2, "description"):
        docker.show_description()
    elif funzione1(2, "configuration"):
        docker.show_configuration()
    elif funzione1(2, "about"):
        docker.show_about()
    elif funzione1(2, "images"):
        docker.show_images()
    elif funzione1(2, "containers"):
        docker.show_containers()
    elif funzione1(2, "network"):
        docker.show_network()
    elif funzione1(2, "volumes"):
        docker.show_volumes()
    elif funzione1(2, "volumes"):
        docker.show_dockerfile()
    elif funzione1(2, "list"):
        docker.list()
    else:
        docker.show()
if funzione1(1, "git"):
    if funzione1(2, "list"):
        docker.list()
    else:
        git.show() 
