import sys
from colors import *

#Classic Functions 
def about():
  print("This is docker")
def show():
  print("")
def list():
  print("[description, configuration, about, in, images, containers, network, volumes, dockerfile]")


#get the name of file from the path e.g. path="/home/user/script.py" return script.py
app=sys.argv[0].split("/")
file_name = app[len(sys.argv[0].split("/"))-1]

if file_name == "docker.py" and len(sys.argv) > 1 and sys.argv[1] == "show":
  show()
if file_name == "docker.py" and len(sys.argv) > 1 and sys.argv[1] == "list":
  list()