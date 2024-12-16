import sys
from colors import *

#Functions 
def show_description():
  print(LIGHTCYANBOLD, "Description")
  print(LIGHTCYAN, "Docker is a set of platform as a service (PaaS) products that use OS-level virtualization")
  print("to deliver software in packages called containers. The software that hosts the containers")
  print("is called Docker Engine. It was first started in 2013 and is developed by Docker, Inc.")
  print("Docker use the Open Container Initiative (OCI) standard compatible with podman.")

  scheme="""
  _____________  _____________  _____________
  |  APP #1   |  |  APP #2   |  |  APP #3   |
  | BIN/LIBS  |  | BIN/LIBS  |  | BIN/LIBS  |   _____________  _____________  _____________
  | GUEST OS  |  | GUEST OS  |  | GUEST OS  |   |  APP #1   |  |  APP #2   |  |  APP #3   |
  |           |  |           |  |           |   | BIN/LIBS  |  | BIN/LIBS  |  | BIN/LIBS  |
  -------------------------------------------   -------------------------------------------
  |                HYPERVISOR               |   |               DOCKER DAEMON             |
  |          HOST OPERETING SYSTEM          |   |          HOST OPERETING SYSTEM          |
  |               INFRACTURE                |   |               INFRACTURE                |
  -------------------------------------------   -------------------------------------------
              VIRUTUAL MACHINE                              DOCKER CONTAINERS
  """
  print(scheme)
def show_configuration():
  print(ROSEBOLD, "Docker configuration", ROSE)
  print("1. curl -sSL https://get.docker.com | sh  -  Docker Installation")
  print("2. docker -v  -  verify if docker installed")
  print("3. sudo groupadd docker  -  create a new group call docker")
  print("4. sudo usermod -aG docker $USER  -  add $USER to tocker group")
def show_about():
  print(YELLOWBOLD, "About Docker", YELLOW)
  print("docker events  -  Get real time events from the server")
  print("docker info  -  Display system-wide information")
  print("docker manifest  -  NAN")
  print("docker version  –  Show the Docker version information")
  print("The docker files are stored in /var/lib/docker")
def show_in():
  print(GREENBOLD, "First Steps", GREEN)
  print("docker search <image>  –  Search the Docker Hub for images")
  print("docker pull <image>  –  Pull an image or a repository from a registry")
  print("docker push  –  Push an image or a repository to a registry")
  print("docker start <container>  –  Start one or more stopped containers")
  print("docker run -dit --name=<name of conatiner>  -v </local-path:/container-path> -p <local-port:docker-port>  –  Run a command in a new container, [dit=> detach|interactive|tty]")
  print("docker attach <container>  –  Attach to a running container")
  print("docker exec -t <container> <console (bash,sh,..)> -c <command>  –  Run a command in a run-time container [t=> tty]")
  print("Ctrl + p && Crtl + q–  Correct way to detach from a container without stopping it")
def show_images():
  print(REDBOLD, "Manage Images", RED)
  print("docker tag <old-repo:oldVersion> <new-repo:newVersion>  -  Create a tag name that refers to source image")
  print("docker save <path> <image>  –  Save Docker image to .tar file specified by path")
  print("docker build -t <image_name> <path>  –  Build an image from a Docker file [t=> tty]")
  print("docker images  –  List all Docker images")
  print("docker rmi <image>  –  Remove Docker image")
  print("docker image history <image>  -  Show the history of an image")
  print("docker commit <old name contaienr> <new name image>  -  Create a new image from a container's changes")
def show_containers():
  print(WHITEBOLD,"Manage Containers", WHITE)
  print("docker export <container> | gzip > <container>.tar.gz  -  Export container")
  print("docker rename <oldContainerName> <newContainerName>  -  Rename a container")
  print("docker restart <container>  -  Restart one or more containers")
  print("docker rm <container_id>  –  Removes Container")
  print("docker container prune  -  Delete containters")
  print("docker pause <container>  -  Pause all processes within one or more containers")
  print("docker unpause <container>  -  Unpause all processes within one or more containers")
  print("docker top <container>  -  Display the running processes of a container")
  print("docker ps  –  Show running containers [l=>latest container created, a=>all]")
  print("docker inspect <container>  -  Return low-level information on Docker objects")
def show_network():
  print(PURPLEBOLD, "Network", PURPLE)
  print("There are three main docker networks:")
  print(PURPLEBOLD, "[Bridge]", PURPLE, "is the default network driver. If you don’t specify a driver, this is the type of network you are creating.")
  print("Theese networks are usually used when your applications run in standalone containers that need to communicate.")
  print(PURPLEBOLD, "[Host]", PURPLE, "is For standalone containers, remove network isolation between the container and the Docker host.")
  print("It use the host’s networking directly.")
  print(PURPLEBOLD, "[None]", PURPLE, "disable all networking. Usually used in conjunction with a custom network driver. none is not available for swarm services.")
  print(PURPLEBOLD, "[Macvlan]", PURPLE, "networks allow you to assign a MAC address to a container, making it appear as a physical device on your network.")
  print("The Docker daemon routes traffic to containers by their MAC addresses. Using the macvlan driver is sometimes the best choice when dealing with legacy")
  print("applications that expect to be directly connected to the physical network, rather than routed through the Docker host’s network stack. See Macvlan networks.")
  print("docker network ls")
  print("docker network inspect <network name>")
  print("docker run -dit -net <host_port:container_port> - ")
  print("docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 macvlan")
  print("docker run -d --network macvlan --ip 192.168.1.x --name <name of container> <image>")
def show_volumes():
  print(BLUEBOLD, "Volumes", BLUE)
  print("docker volume ls  -  List volumes")
  print("docker volume create  -  Create a volume")
  print("docker volume inspect  -  Display detailed information on one or more volumes")
  print("docker volume prune  -  Remove all unused local volumes")
  print("docker volume rm  -  Remove one or more volumes")
  print("docker run -dit --volume <hostDir>:</containerDir> <image>")
  print("docker run -dit --volume <hostDir or vitualVolume>:</containerDir>:ro <image> - Read Only")
  print("docker run -dit --device=/dev/sda2 --privileged --name dev2 debian")
  print("docker system prune -a  -  Remove unused data")
def show_dockerfile():
  print(LIGHTCYANBOLD, "Instructions", LIGHTCYAN)
  print("A Dockerfile is written in the Domain-specific language (DSL)")
  print("Docker buid has a own cache ... ")
  print("# COMMENTS")
  print("ENV")
  print("Everey Dockerfile have to start with FROM instruction that specifies the Parent Image from which you are building.")
  print("1) ADD a file to image")
  print("-) ARG -  define the name of a parameter and its default value")
  print("2) CMD - Execute the command in start phase")
  print("3) COPY")
  print("4) FROM a")
  print("    • FROM <nome_immagine>")
  print("    • FROM <nome_immagine>:<tag>")
  print("    • FROM <nome_immagine>@<hash>")
  print("5) ENTRYPOINT")
  print("6) EXPOSE")
  print("7) LABEL")
  print("8)RUN - Execute the command in build  phase")
  print("9)VOLUME")
  #echo "RESTART POLICY")
  print("ssh")
  print("docker run -dit --network macvlan --ip 192.168.1.77 --name alessio debian_full")

#Classic Functions 
def about():
  print("This is docker")
def show():
  show_description()
  show_configuration()
  show_about()
  show_in()
  show_images()
  show_containers()
  show_network()
  show_volumes()
  show_dockerfile()
def list():
  print("[description, configuration, about, in, images, containers, network, volumes, dockerfile]")


#get the name of file from the path e.g. path="/home/user/script.py" return script.py
app=sys.argv[0].split("/")
file_name = app[len(sys.argv[0].split("/"))-1]

if file_name == "docker.py" and len(sys.argv) > 1 and sys.argv[1] == "show":
  show()
if file_name == "docker.py" and len(sys.argv) > 1 and sys.argv[1] == "list":
  list()

print("docker stop $(docker ps -a -q)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
